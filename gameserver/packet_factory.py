from dataclasses import dataclass


@dataclass
class SessionInfoPacket:

    session_id: str

    session_type: int

    twitch_scene: str

    game_type: int

    variation_id: int

    num_connections: int

    num_players: int

    max_players: int

    allow_consumables: bool

    force_respawn: bool


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


class PacketFactory:

    @staticmethod
    def session_info(session):

        return SessionInfoPacket(

            session_id=str(session.id),

            session_type=session.session_type,

            twitch_scene=session.map_name,

            game_type=session.game_type,

            variation_id=session.variation_id,

            num_connections=len(session.players),

            num_players=len(session.players),

            max_players=session.max_players,

            allow_consumables=session.allow_consumables,

            force_respawn=session.force_respawn
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

            position=player.position,

            look_at=player.look_at
        )

    @staticmethod
    def create_remote_player(player):

        return CreateRemotePlayerPacket(

            timestamp=player.timestamp,

            player_id=player.player_id,

            account_id=str(player.account_id),

            account_name=player.account_name,

            health=player.health,

            armor=player.armor,

            team=player.team,

            flags=player.flags,

            current_weapon_slot=player.current_weapon_slot,

            waiting_to_respawn=player.waiting_to_respawn,

            position=player.position,

            look_at=player.look_at
        )