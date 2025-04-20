from arduinoWithSonar import ArduinoWithSonar
from pyfirmata2 import util
import time
curr_time = time.time()

board = ArduinoWithSonar("COM5")
it = util.Iterator(board)
it.start()
curr_measure = 0

while True :
    new_measure = board.get_sonar_measurement()
    if new_measure == 0 :
        continue
    
    if new_measure != curr_measure :
        print(new_measure) 
        curr_measure = new_measure