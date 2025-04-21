# SonarSupportForPyFirmata2

This project is a result of the curriculum planners at my university being fucking idiots. They have decided that the best way to learn working 
with Arduino’s was not to do it the regular way, just using Arduino Sketch which has thousands of pages of documentation and fan made tutorials. 
But to instead use a sketchy ass python library whose code looks like a christmas tree. To add insult to injury they also require us that we make use 
of a HC-SR04 Sonar, something that.... surprise surprise this 700 line 1 class shithole that calls itself pyFirmata2 does not support. 
Thus I had to modify the firmata image (witch is actually what's being run on the arduino and sends data to the library) and add a supporting class on top of the library itself
so I could get full points for the assignment. Anyway if you are also required to use pyFirmata2 or (for some reason) use it voluntarily. Here's a simple solution for adding support for sonars.

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
