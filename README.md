# HiFly obstacle avoidance stack
This is a custom hardware sensor module to bring obstacle avoidance capabilities to small robotics. It is a fully independent module based on Arduino Nano IoT 33.


![image info](Assets/module_only_crop.jpg)


## Features
General
 - Wifi 
 - Bluetooth
 - Independent Lipo battery based power system
 - 7 RBG LED ring for display or user interaction
 - Total weight only 35g

 Sensing
 - 360 degree lateral ToF sensing using 6 wide FoV channels
 - 1 narrow ToF sensor facing forward
 - 6 axis IMU

<br/><br/>
## Required knowledge to do the assembly
- 3D printing 
- Arduino/MCU programming
- Electronics - soldering, dupont connectors, etc

<br/><br/>
## Links
- [Assembly guide](ASSEMBLY.md)
- HiFly repo

<br/><br/>

# Parts list

### MCU
- [Arduino Nano iot 33](https://www.amazon.ca/Arduino-Nano-33-IoT/dp/B07VW9TSKD/ref=sr_1_2?keywords=arduino+nano+iot+33&qid=1654530366&sr=8-2)

### Sensors
- 2 x [OPT3101](https://www.robotshop.com/ca/en/3-channel-wide-fov-time-of-flight-distance-sensor-opt3101-no-headers.html)
- [ToF VL53L0X](https://www.amazon.ca/gp/product/B097SJ37DX/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

### Display
- [Adafruit NeoPixel Jewel](https://www.amazon.ca/gp/product/B00Q9R8QUO/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) 

### Power
- [Battery, connector](https://www.amazon.ca/gp/product/B08NYDQ3HZ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [Power converter](https://leeselectronic.com/en/product/15123-pololu-5v-step-up-voltage-regulator-u1v11f5.html)

### Circuit components (available in many kits)
- 30 AWG wires
- 2 NPN 8050 transistors
- 3 10k ohm resistors
- Dupoint wiring kit (be able to make 2x7, 1x6 connections)
- switch (available in many kits)

### Assembly
- 3D printing tools
- soldering tools
- tweezers, clippers, etc very useful