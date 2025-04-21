from arduinoWithSonar import ArduinoWithSonar
from pyfirmata2 import util

#set up board
board = ArduinoWithSonar("COM5")

#start iterator
#NOTE this is needed to continuesly update the sonar data
board.samplingOn()

curr_measure = 0

#setting up the sonar with the trigger- and echopin, plus capture hsitory size
board.sonar_config(8, 9, sonar_capture_history_size=1)

while True :
    new_measure = board.get_sonar_measurement()
    
    #only print new measures if they have changed
    if new_measure != curr_measure :
        print(new_measure) 
        curr_measure = new_measure