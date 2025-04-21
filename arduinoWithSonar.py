from pyfirmata2 import Arduino
import threading
import sys
import time

class messageTypes :
    # outgoing messages to firmata
    SONAR_CONFIG = 0x00 #message to firmata to configure the sonar sensor with the given pin numbers
    SONAR_REQUEST = 0x01 #message to firmata to request sonar data 

    # incoming messages from firmata
    SONAR_RESPONSE = 0x02 #message FROM firmata with sonar data

class ArduinoWithSonar(Arduino) :
    def __init__(self : int = 1, /, *args, **kwargs) :
        super().__init__(*args,**kwargs)

        self.__sonar_measurements : list[int] = []
        self.__sonar_capture_history_size = 1
        self.__fast_measurement = 0

        self.__sonarthread : threading.Thread = threading.Thread(target=self.__send_sonar_request)
        self.__sonarthread_running : bool = False
        self.__sonarthread.daemon = True

    #add handler for incoming sonar data (overwritten)
    def _set_default_handlers(self) -> None:
        self.add_cmd_handler(messageTypes.SONAR_RESPONSE, self.__sonar_data_handler)
        super()._set_default_handlers()

    #data handler
    def __sonar_data_handler(self, distance : int) -> None:
        #set a fast measurement without mode filtering
        self.__fast_measurement = distance

        #update saved measures
        if len(self.__sonar_measurements) == self.__sonar_capture_history_size :
             self.__sonar_measurements.pop(0)
        self.__sonar_measurements.append(distance)

    #sonar configuration (user called function)
    def sonar_config(self, trigger_pin : int, echo_pin : int, sonar_capture_history_size : int = 1) -> None:
        #setting the amounth of saved measures at a time
        if type(sonar_capture_history_size == int and sonar_capture_history_size > 0) :
            self.__sonar_capture_history_size : int = sonar_capture_history_size

        if type(trigger_pin) != int or type(echo_pin) != int :
            print("PIN NUMBERS ARE NOT VALID, IGNORING REQUEST")
            return
        
        data : bytearray = bytearray([trigger_pin, echo_pin])
        self.send_sysex(messageTypes.SONAR_CONFIG, data)
    
    #request for latest measurement (user called function)
    def get_sonar_measurement(self) -> int :
        #return mode off all saved measures
        if len(self.__sonar_measurements) < 1 :
            return 0
        
        #if history size is 1, return a fast mesaurement without mode filtering
        if self.__sonar_capture_history_size == 1 :
            return self.__fast_measurement
        
        return max(self.__sonar_measurements, key=self.__sonar_measurements.count)
    
    #send message to firmata to trigger the sonar sensor
    def __send_sonar_request(self) -> None :
        while True :
            try :
                #send_sysex is an arduino function that sends messages to firmata with data
                #in this case we dont need to send additional data
                self.send_sysex(messageTypes.SONAR_REQUEST,bytearray([])) # request sonar data from firmata

                #turing this value lower will result in the system sending out request faster then it can handle incomming data
                time.sleep(0.2)
            except KeyboardInterrupt:
                sys.exit()

    def samplingOn(self, sample_interval=19):
        # enables sampling
        super().samplingOn(sample_interval)
        if not self.__sonarthread_running:
            self.__sonarthread.start()
            self.__sonarthread_running = True

    def samplingOff(self):
        super().samplingOff()
        # disables sampling
        if not self.__sonarthread:
            return
        if self.__sonarthread_running:
            self.__sonarthread.stop()
            self.__sonarthread.join()
            self.__sonarthread_running = False

    