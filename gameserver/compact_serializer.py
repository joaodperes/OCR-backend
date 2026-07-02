from gameserver.serialization import BinaryWriter

class CompactSerializer:

    @staticmethod
    def serialize(packet):

        writer = BinaryWriter()

        packet.serialize(writer)

        return writer.get_bytes()