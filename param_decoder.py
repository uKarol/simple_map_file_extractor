import cstruct

class Packet(cstruct.MemCStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __def__ = """

    struct Packet
    {
        uint16_t scenario;
        uint16_t param;
        uint16_t datasize;
    };

    """

class packet_reader:

    def __init__(self, com):
        self.com = com

    def connect(self):
        self.com.connect()

    def disconnect(self):
        self.com.disconnect()
        
    def receive_packet(self):
        my_packet = Packet()
        byte = self.com.read_bytes(1)
        while(byte != b'U'):
            byte = self.com.read_bytes(1)
        frame = self.com.read_bytes(6)
        my_packet.unpack(frame)
        data_frame = self.com.read_bytes(my_packet.datasize)
        return (my_packet, data_frame)
