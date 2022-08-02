from djitellopy import Tello
import time   
from ObsAvoid import calculate_drone_velocity



if __name__ == "__main__":

    LIVE_FLAG = False

    tello = Tello()

    if(LIVE_FLAG):

        tello.connect()
        tello.takeoff()
        tello.start_obs_send()

    forward_backward_velocity = 0
    left_right_velocity = 0
    up_down_velocity = 0


    try:
        while(True):
            forward_backward_velocity = 0
            left_right_velocity = 0
            up_down_velocity = 0

            if(len(tello.obs_avoid_info) > 0 and (time.time() - tello.obs_avoid_last_received_timestamp) < 2): #and (time.time() - tello.obs_avoid_last_received_timestamp) > 0.1):

                # Get horizontal avoidance velocity vector
                avoid_velocity = calculate_drone_velocity(tello.obs_avoid_info[:-1])
                print(tello.obs_avoid_info, avoid_velocity)
                left_right_velocity = avoid_velocity[0]
                forward_backward_velocity = avoid_velocity[1]

                # # Forward facing beam ToF threshold
                # if(tello.obs_avoid_info[-1] < 750):
                #     up_down_velocity = -15
                # else:
                #     up_down_velocity = 15

                if(not LIVE_FLAG):
                    time.sleep(0.1)
                else:
                    tello.send_rc_control(int(left_right_velocity), int(forward_backward_velocity), int(up_down_velocity), 0)

            else:
                continue
            

    except KeyboardInterrupt:
        tello.land()