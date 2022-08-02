# Arduino packages to download
- WiFiNINA
- Adafruit NeoPixel
- DFRobot_VL53L0X
- OPT3101
# 3D printing the frame
- The frame is one large part, can be printed facing downwards (LED side on bed) and only using supports for the 'chimney' and LED ring.

- There is another small part to pop into the back, used to enclose the frame.

- When using with the DJI Tello drone, there is also a clip-mount component available.


# OPT3101 same I2C address workaround
The OPT3101 sensors share a hardcoded I2C address, which is an issue when we want to use two or more of them at the same time. The workaround used here is to use transistors to control which sensor the SDA line is connected to. The transistors can be toggled through the firmware to select which sensor to read from.


# Preparing the electronics
- Solder the two resistors and NPN transistors together according to the schematic. You can also add a heatshrink wrap the whole resistor branch.

- - <img src="Assets/1_crop.jpg" alt="drawing" width="500"/>
- - <img src="Assets/2_crop.jpg" alt="drawing" width="500"/>

- Solder this combined component to the arduino according to the schematic. Try to have the component as flat as possible to conserver space.

- - <img src="Assets/3_crop.jpg" alt="drawing" width="500"/>

- Solder the 4 Vdd wires and 5 GND wires to the arduino, apply shrinkwrap.
- - <img src="Assets/4_crop.jpg" alt="drawing" width="500"/>

- Solder the Vin and 3 I2C scl wires to the arduino.
- - <img src="Assets/5_crop.jpg" alt="drawing" width="500"/>

- Solder the 3 I2C sda wires and the 1 LED signal wire to the arduino.
- - <img src="Assets/6_crop.jpg" alt="drawing" width="500"/>

- With all the arduino wires soldered, the next step is to prepare the wires for each component by tieing them together.
- - <img src="Assets/7_crop.jpg" alt="drawing" width="500"/>

- Once the 4 wire batches are wrapped, the arduino can be inserted into the frame. A tweezer is useful for this step as each wire batch has to go through its corresponding slot.
- - <img src="Assets/8_crop.jpg" alt="drawing" width="500"/>
- - <img src="Assets/9_crop.jpg" alt="drawing" width="500"/>
- - <img src="Assets/10_crop.jpg" alt="drawing" width="500"/>

- Once the arduino is in the frame and the wires are all through the right slots, the power system components can be prepared and soldered to the GND and Vin wires of the arduino.
- A dummy program can be used to test wether the power system is working to power the arduino. Beware though that with the loads connected there can still be issues.
- - <img src="Assets/11_crop.jpg" alt="drawing" width="500"/>

- If the power is working, the next step is to attach the components. First, the LED ring can be directly soldered to its wires, then use some adhesive to mount it into its slot.

- - <img src="Assets/12_crop.jpg" alt="drawing" width="500"/>

- Next, a 1x6 dupont connecting should be made for the front facing ToF sensor.

- - <img src="Assets/13_crop.jpg" alt="drawing" width="500"/>


- Finally, a 2x7 dupont connection should be made for the 2 OPT3101 sensors on top. Make sure to attach the wires to the right positions as the two sensor pins are not aligned - eg the Vdd pins are not next to eachother.

- - <img src="Assets/14_crop.jpg" alt="drawing" width="500"/>

- Once the dupont connectors are pushed into the frame, the sensors can be simply plugged in. For the ToF sensor, a resistor should be soldered accross from the Vin to the shutdown pin before plugging it in.

- - <img src="Assets/15_crop.jpg" alt="drawing" width="500"/>


- The 2 OPT3101 sensor can be simply plugged in from the top. If there is not enough friction to keep the dupont connector in place, you can use the tweezers to support it from the bottom while plugging the sensors in.
![image info](Assets/module_only_crop.jpg)


- Finally, the whole system can be tested with the battery plugged in. If everyhting is working, the battery plug can be superglued to its mounting spot and the back cover part can be snapped onto the back of the frame. The assembly is done!
-- <img src="Assets/hatch_crop.jpg" alt="drawing" width="500"/>
