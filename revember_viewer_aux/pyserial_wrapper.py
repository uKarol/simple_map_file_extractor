import serial

class pyserial_wrapper:
    def __init__(self):
        pass

    def connect(self, port, baud):
        try:
            self.ser = serial.Serial(port, baud)
        except:
            raise ConnectionError("CPYSERIAL ERROR \n CANNOT OPEN SERIAL PORT")
    
    def disconnect(self):
        try:
            self.ser.close()
        except:
            raise ConnectionError("PYSERIAL ERROR \n CANNOT CLOSE SERIAL PORT")

    def read_bytes(self, number):
        try:
            ret_val = self.ser.read(number)
        except:
            raise ConnectionError("PYSERIAL ERROR \n CANNOT READ BYTES - CONNECTION LOST")
        return ret_val