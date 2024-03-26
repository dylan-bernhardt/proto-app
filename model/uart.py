from typeguard import typechecked
import serial
import threading

class Data :
    @typechecked
    def __init__(self, com : str, baudrate: int) -> None: 
        self.a= 0
        self.__concentration = 0
        self.__level = 0
        self.__ser = serial.Serial(com, baudrate, timeout=100)
        thread = threading.Thread(target= self.read_data, args=(self.__ser,))
        thread.daemon = True
        thread.start()
        
    @typechecked
    def get_concentration(self) -> int :
        return self.__concentration

    @typechecked
    def get_level(self) -> int : 
        return self.__level

    @typechecked
    def read_data(self, ser: serial.Serial) -> None :
        while True : 
            self.__concentration = int(ser.readline())   


    
