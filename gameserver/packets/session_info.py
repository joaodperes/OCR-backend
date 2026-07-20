from dataclasses import dataclass
import uuid


@dataclass
class SessionInfoPacket:

    session_id: uuid.UUID

    session_type: int

    twitch_scene: str

    game_type: int

    variation_id: int

    num_connections: int

    num_players: int

    max_players: int

    allow_consumables: bool

    force_respawn: bool