from dataclasses import dataclass


@dataclass
class CreateRemotePlayerPacket:

    timestamp: int

    player_id: int

    account_id: str

    account_name: str

    health: int

    armor: int

    team: int

    flags: int

    current_weapon_slot: int

    waiting_to_respawn: bool

    position: tuple

    look_at: tuple

    pwn_loadout: list

    applied_buffs: list

    skills: object

    avatar_loadout: object

    weapon_loadout: object

    def serialize(self, writer):

        writer.write_int(self.timestamp)

        writer.write_int(self.player_id)

        writer.write_guid(self.account_id)

        writer.write_string(self.account_name)

        writer.write_uint16(self.health)

        writer.write_uint16(self.armor)

        writer.write_byte(self.team)

        writer.write_uint16(self.flags)

        writer.write_byte(self.current_weapon_slot)

        writer.write_bool(self.waiting_to_respawn)

        writer.write_float(self.position[0])
        writer.write_float(self.position[1])
        writer.write_float(self.position[2])

        writer.write_byte(self.look_at[0])
        writer.write_byte(self.look_at[1])
        writer.write_byte(self.look_at[2])

        writer.write_byte(len(self.applied_buffs))

        for buff in self.applied_buffs:

            buff.serialize(writer)

        writer.write_byte(len(self.pwn_loadout))

        for item in self.pwn_loadout:

            writer.write_string(item)

        self.skills.serialize(writer)

        self.avatar_loadout.serialize(writer)

        self.weapon_loadout.serialize(writer)