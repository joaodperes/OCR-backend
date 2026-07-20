from dataclasses import dataclass

@dataclass
class CreatePlayerPacket:

    player_id: int
    team: int

    health: int
    full_health: int
    armor: int

    current_weapon_slot: int

    position: tuple
    look_at: tuple

    avatar_loadout: object
    weapon_loadout: object
    weapon_ammo: object

    applied_buffs: list

    def serialize(self, writer):

        writer.write_int(self.player_id)

        writer.write_byte(self.team)

        writer.write_uint16(self.health)

        writer.write_uint16(self.full_health)

        writer.write_uint16(self.armor)

        writer.write_byte(self.current_weapon_slot)

        writer.write_float(self.position[0])
        writer.write_float(self.position[1])
        writer.write_float(self.position[2])

        writer.write_byte(self.look_at[0])
        writer.write_byte(self.look_at[1])
        writer.write_byte(self.look_at[2])

        self.avatar_loadout.serialize(writer)

        self.weapon_loadout.serialize(writer)

        self.weapon_ammo.serialize(writer)

        writer.write_byte(len(self.applied_buffs))

        for buff in self.applied_buffs:

            buff.serialize(writer)