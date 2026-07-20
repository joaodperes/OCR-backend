from dataclasses import dataclass
from uuid import UUID


# ---------------------------------------------------------
# Session Info
# ---------------------------------------------------------

@dataclass
class SessionInfoPacket:

    session_id: UUID

    session_type: int

    twitch_scene: str

    game_type: int

    variation_id: int

    num_connections: int

    num_players: int

    max_players: int

    num_spectators: int

    max_spectators: int

    allow_consumables: bool

    force_respawn: bool


# ---------------------------------------------------------
# Local Player
# ---------------------------------------------------------

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

    avatar_loadout: dict

    weapon_loadout: dict

    weapon_ammo: dict

    buffs: list


# ---------------------------------------------------------
# Remote Player
# ---------------------------------------------------------

@dataclass
class CreateRemotePlayerPacket:

    timestamp: int

    player_id: int

    account_id: str

    name: str

    health: int

    armor: int

    team: int

    flags: int

    current_weapon_slot: int

    waiting_to_respawn: bool

    position: tuple

    look_at: tuple

    pwn_loadout: list

    buffs: list

    skills: dict

    avatar_loadout: dict

    weapon_loadout: dict


# ---------------------------------------------------------
# Factory
# ---------------------------------------------------------

class PacketFactory:

    @staticmethod
    def session_info(session):

        return SessionInfoPacket(

            session_id=session.id,

            session_type=session.session_type,

            twitch_scene=session.map_name,

            game_type=session.game_type,

            variation_id=session.variation_id,

            num_connections=session.num_connections,

            num_players=session.num_players,

            max_players=session.max_players,

            num_spectators=session.num_spectators,

            max_spectators=session.max_spectators,

            allow_consumables=session.allow_consumables,

            force_respawn=session.force_respawn,
        )

    @staticmethod
    def create_player(player):

        return CreatePlayerPacket(

            player_id=player.player_id,

            team=player.team,

            health=player.health,

            full_health=player.full_health,

            armor=player.armor,

            current_weapon_slot=player.current_weapon_slot,

            position=(
                player.position.x,
                player.position.y,
                player.position.z,
            ),

            look_at=(
                player.look_at.x,
                player.look_at.y,
                player.look_at.z,
            ),

            avatar_loadout={},

            weapon_loadout={},

            weapon_ammo={},

            buffs=[],
        )

    @staticmethod
    def create_remote_player(player):

        return CreateRemotePlayerPacket(

            timestamp=0,

            player_id=player.player_id,

            account_id=str(player.account_id),

            name=player.name,

            health=player.health,

            armor=player.armor,

            team=player.team,

            flags=0,

            current_weapon_slot=player.current_weapon_slot,

            waiting_to_respawn=False,

            position=(
                player.position.x,
                player.position.y,
                player.position.z,
            ),

            look_at=(
                player.look_at.x,
                player.look_at.y,
                player.look_at.z,
            ),

            pwn_loadout=[],

            buffs=[],

            skills={},

            avatar_loadout={},

            weapon_loadout={},
        )