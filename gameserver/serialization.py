import io
import struct


class BinaryWriter:

    def __init__(self):

        self.buffer = io.BytesIO()

    def write_int(self, value):
        self.buffer.write(struct.pack("<i", value))

    def write_uint16(self, value):
        self.buffer.write(struct.pack("<H", value))

    def write_byte(self, value):
        self.buffer.write(struct.pack("<B", value))

    def write_bool(self, value):
        self.buffer.write(struct.pack("<?", value))

    def write_float(self, value):
        self.buffer.write(struct.pack("<f", value))

    def write_string(self, value):

        encoded = value.encode("utf-8")

        self.write_7bit_int(len(encoded))

        self.buffer.write(encoded)

    def write_guid(self, guid):

        self.write_string(str(guid))

    def write_7bit_int(self, value):

        while value >= 0x80:

            self.write_byte((value & 0x7F) | 0x80)

            value >>= 7

        self.write_byte(value)

    def get_bytes(self):

        return self.buffer.getvalue()