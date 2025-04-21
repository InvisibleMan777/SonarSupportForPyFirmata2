# SonarSupportForPyFirmata2

This project is an extension of [pyFirmata2](https://github.com/berndporr/pyFirmata2/tree/master). A library that makes working an [Arduino](https://www.arduino.cc/) with python possible. 
This extension adds to ability to receive data from a connected sonar ([HC-SR04](https://projecthub.arduino.cc/Isaac100/getting-started-with-the-hc-sr04-ultrasonic-sensor-7cabe1) specifically). 
The cause of me starting this project is my university forcing me to use pyFirmata2 while also only giving me full point on an assignment if I use a sonar,
something that.... surprise surprise this 700 line 1 class 0 documentation disappointment of a library whose code looks like a christmas tree does not support. 
Thus I had to modify the firmata image (witch is actually what's being run on the arduino and sends data to the library) and add a supporting class on top of the library itself
Anyway if you are also required to use pyFirmata2 or (for some reason) use it voluntarily. Here's a simple solution for adding support for sonars.


## Usage
### hardware
Sonar connection (from sonar to arduino)
- connect vcc to 5v
- connect gnd to gnd
- connect echo and trigger to 2 digital pins
### software
- run the `modifiedFirmata.ino` file in the Arduino IDE on your arduino
- pip install [pyFirmata2](https://github.com/berndporr/pyFirmata2/tree/master)
- Include `util` from pyFirmata2 in your project
- Include `ArduinoWithSonar` from the `arduinoWithSonar.py` file in your project
- initialise your board as an `ArduinoWithSonar` object
- initialise the iterator  (`it = util.Iterator(board)`)
- start the iterator (`it.start()`)
  - *NOTE: The iterator is needed to continuously measure with the sonar*
- Have fun with the extra functionality
- see `example.py` for further clarification

## Important functions

### sonar_config(`trigger_pin`, `echo_pin`, `sonar_cature_history size (default=1`)
Sets up the sonar. 
for now only one sonar is supported at a time

if a `sonar_capture_history_size` above 1 is set then the sonar will return the mode of the last `sonar_capture_history_size` measurements for greater accuracy.
However this comes to the detriment of the speed of the updates

### get_sonar_measurement()
returns the latest measured distance in centimeters


## pyFirmata2
This software is an extention of the pyFirmata2 library.
For any documentation (good luck) about pyFirmata2 itself see
https://github.com/berndporr/pyFirmata2/tree/master
