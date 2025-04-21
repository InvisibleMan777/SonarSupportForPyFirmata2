from arduinoWithSonar import ArduinoWithSonar
from pyfirmata2 import util

#set up board
board = ArduinoWithSonar("COM5")

#start iterator
#NOTE this is needed to continuesly updating the sonar data
it = util.Iterator(board)
it.start()

curr_measure = 0

#setting up the sonar with the trigger- and echopin
board.sonar_config(8, 9)

while True :
    new_measure = board.get_sonar_measurement()

    #skip 0 values (they sometimes show up as a result of hardware failure)
    if new_measure == 0 :
        continue
    
    #only print new measures if they have changed
    if new_measure != curr_measure :
        print(new_measure) 
        curr_measure = new_measure