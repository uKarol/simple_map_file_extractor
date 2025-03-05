import cstruct

class HeaderFrame(cstruct.MemCStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __def__ = """

    struct HeaderFrame
    {
        uint16_t scenario;
        uint16_t id;
        uint16_t datasize;
    };

    """

class HeaderDecoder:

    def __init__(self, com):
        self.com = com

    def connect(self):
        self.com.connect()

    def disconnect(self):
        self.com.disconnect()
        
    def receive_packet(self):
        my_header = HeaderFrame()
        byte = self.com.read_bytes(1)
        while(byte != b'U'):
            byte = self.com.read_bytes(1)
        frame = self.com.read_bytes(6)
        my_header.unpack(frame)
        data_frame = self.com.read_bytes(my_header.datasize)
        return (my_header, data_frame)
