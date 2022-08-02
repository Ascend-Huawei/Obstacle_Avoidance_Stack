import numpy as np


MAX_DISTANCE = 1000    # max range threshold of sensors in mm - bounded on arduino
MIN_VECTOR = 0
MAX_VECTOR = (2271)    # largest possible vector in one direction
MAX_VELOCITY = 70      # each output velocity component will be at most this value 
FORWARD_BACKWARD_THRESHOLD = 550
SQUEEZE_THRESHOLD = 400
MIN_CORNER_DIST_THRESH = 400

dir_vectors = np.asarray([[4,8], [9,0], [4,-8], [-4,-8], [-9,0], [-4, 8]], dtype=np.float32)   # 6 sensor directions with unit vector size of 9
# convert to unit vectors
for i, vector in enumerate(dir_vectors):
    dir_vectors[i] = vector / np.linalg.norm(vector)


def calculate_resultant_vector(magnitudes):
    magnitudes = np.asarray(magnitudes, dtype=int)

    if(magnitudes[1] < SQUEEZE_THRESHOLD and magnitudes[4] < SQUEEZE_THRESHOLD):
        if((magnitudes[0] + magnitudes[5]) > (magnitudes[2] + magnitudes[3])):
            magnitudes[2] = 1
            magnitudes[3] = 1
        else:
            magnitudes[0] = 1
            magnitudes[5] = 1

    else:
        if(magnitudes[0] < FORWARD_BACKWARD_THRESHOLD and magnitudes[5] < FORWARD_BACKWARD_THRESHOLD):
            magnitudes[0] = 1
            magnitudes[5] = 1
        
        if(magnitudes[2] < FORWARD_BACKWARD_THRESHOLD and magnitudes[3] < FORWARD_BACKWARD_THRESHOLD):
            magnitudes[2] = 1
            magnitudes[3] = 1

        if(magnitudes.sum() > 4000):
            if(magnitudes[magnitudes.argmin()] < MIN_CORNER_DIST_THRESH):
                magnitudes[magnitudes.argmin()] = 1
                
        
        if(magnitudes[1] < SQUEEZE_THRESHOLD and magnitudes[4] < SQUEEZE_THRESHOLD):
            if((magnitudes[0] + magnitudes[5]) > (magnitudes[2] + magnitudes[3])):
                magnitudes[2] = 1
                magnitudes[3] = 1
            else:
                magnitudes[0] = 1
                magnitudes[5] = 1



    inversed_magnitudes = MAX_DISTANCE - magnitudes.reshape(-1, 1)
    resultant_vector = (inversed_magnitudes * dir_vectors).sum(0)
    return resultant_vector


def calculate_velocity(res_obstacle_vector):
    obs_sum = np.linalg.norm(res_obstacle_vector)

    if(obs_sum == 0):
        return [0,0]

    else:
        reflected_vector = -res_obstacle_vector
        velocity_percent = (reflected_vector - MIN_VECTOR) / (MAX_VECTOR - MIN_VECTOR)
        return velocity_percent * MAX_VELOCITY


def calculate_drone_velocity(magnitudes):
    return calculate_velocity(calculate_resultant_vector(magnitudes))


if __name__ == "__main__":
    mag_vectors = [200,1000,1000,1000,1000,200]

    print("res velocity: ", calculate_drone_velocity(mag_vectors))