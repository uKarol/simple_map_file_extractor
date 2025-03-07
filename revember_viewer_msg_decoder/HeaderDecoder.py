import cstruct

class HeaderReceptionError(Exception):
    """CANNOT ASSEMBLE HEADER - CONNECTION ERROR"""

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

    def parse_header(self, data : bytes):
        my_header = HeaderFrame()
        my_header.unpack(data)
        return my_header
        
    def receive_packet(self):
        try:
            byte = self.com.read_bytes(1)
            while(byte != b'U'):
                byte = self.com.read_bytes(1)
            header = self.parse_header(self.com.read_bytes(6))
            data_frame = self.com.read_bytes(header.datasize)
        except ConnectionError:
            raise HeaderReceptionError("WHEN PROCESSING HEADER FRAME")
        return (header, data_frame)
