from pyfirmata2 import Arduino

class messageTypes :
    # outgoing messages to firmata
    SONAR_CONFIG = 0x00 #message to firmata to configure the sonar sensor with the given pin numbers
    SONAR_REQUEST = 0x01 #message to firmata to request sonar data 

    # incoming messages from firmata
    SONAR_RESPONSE = 0x02 #message FROM firmata with sonar data

class ArduinoWithSonar(Arduino) :
    def __init__(self, *args, **kwargs) :
        super().__init__(*args,**kwargs)

        self.__sonar_measurement : int = 0

    #add handler for incoming sonar data (overwritten)
    def _set_default_handlers(self) -> None:
        self.add_cmd_handler(messageTypes.SONAR_RESPONSE, self.__sonar_data_handler)
        super()._set_default_handlers()

    #data handler
    def __sonar_data_handler(self, distance : int) -> None:
        self.__sonar_measurement = distance

    #sonar configuration (user called function)
    def sonar_config(self, trigger_pin : int, echo_pin : int) -> None:
        if type(trigger_pin) != int or type(echo_pin) != int :
            print("PIN NUMBERS ARE NOT OF TYPE `int`, IGNORING REQUEST")
            return
        data : bytearray = bytearray([trigger_pin, echo_pin])
        self.send_sysex(messageTypes.SONAR_CONFIG, data)
    
    #request for latest measurement (user called function)
    def get_sonar_measurement(self) -> int :
        return self.__sonar_measurement
    
    #send message to firmata to trigger the sonar sensor
    def __send_sonar_request(self) -> None :
        #send_sysex is an arduino function that sends messages to firmata with data
        #in this case we dont need to send additional data
        self.send_sysex(messageTypes.SONAR_REQUEST,bytearray([])) # request sonar data from firmata

    #send sonar_request every itteration (overwritten)
    def iterate(self) -> None :
        self.__send_sonar_request()
        super().iterate()

    