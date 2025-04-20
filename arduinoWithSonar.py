from pyfirmata2 import Arduino
import time

class messageTypes :
    # outgoing messages to firmata
    SONAR_CONFIG = 0x00 #message to firmata to configure the sonar sensor with the given pin numbers
    SONAR_REQUEST = 0x01 #message to firmata to request sonar data (trigger the sonar sensor)

    # incoming messages from firmata
    SONAR_RESPONSE = 0x02 #message FROM firmata with sonar data

class ArduinoWithSonar(Arduino) :
    def __init__(self, *args, **kwargs) :
        super().__init__(*args,**kwargs)

        self.__sonar_measurement : int = 0

    #add handler for incoming sonar data
    def _set_default_handlers(self) :
        self.add_cmd_handler(messageTypes.SONAR_RESPONSE, self.__sonar_data_handler)
        super()._set_default_handlers()

    def __sonar_data_handler(self, distance) :
        self.__sonar_measurement = distance

    #sonar configuration (user called function)
    def sonar_config(self, trigger_pin, echo_pin):
        data : bytearray = bytearray([trigger_pin, echo_pin])
        self.send_sysex(messageTypes.SONAR_CONFIG, data)
    
    #request for latest measurement (user called function)
    def get_sonar_measurement(self) :
        return self.__sonar_measurement
    
    #send message to firmata to trigger the sonar sensor
    def __send_sonar_request(self) :
        self.send_sysex(messageTypes.SONAR_REQUEST,bytearray([])) # request sonar data from firmata

    #send sonar_request every itteration
    def iterate(self):
        self.__send_sonar_request()
        super().iterate()

    