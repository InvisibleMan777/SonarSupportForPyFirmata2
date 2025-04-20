# SonarSupportForPyFirmata2

This project is a result of the curriculum planners at my university being fucking idiots. They have decided that the best way to learn working 
with Arduino’s was not to do it the regular way, just using Arduino Sketch which has thousands of pages of documentation and fan made tutorials. 
But to instead use a sketchy ass python library whose code looks like a christmas tree. To add insult to injury they also require us that we make use 
of a HC-SR04 Sonar, something that.... surprise surprise this 700 line 1 class shithole that calls itself pyFirmata2 does not support. 
Thus I had to modify the firmata image and (witch is actually what's being run on the arduino and sends data to the library) and add a supporting class on top of the library itself
so I could get full points for the assignment. Anyway if you are also required to use pyFirmata2 or (for some reason) use it voluntarily. Here's a simple solution for adding support for sonars.


