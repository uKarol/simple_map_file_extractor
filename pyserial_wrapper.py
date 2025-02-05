import serial

class pyserial_wrapper:
    def __init__(self, port, baud):
        self.ser = serial.Serial(port, baud)

    def connect(self):
        self.ser.open()
    
    def disconnect(self):
        self.ser.close()

    def read_bytes(self, number):
        return self.ser.read(number)