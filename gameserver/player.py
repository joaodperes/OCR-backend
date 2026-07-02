from uuid import uuid4


class Player:

    def __init__(self):

        # Identity

        self.player_id = 0
        self.account_id = uuid4()
        self.account_name = "Player"

        # Gameplay

        self.team = 0

        self.health = 100
        self.full_health = 100
        self.armor = 0

        self.current_weapon_slot = 0

        self.position = (0.0, 0.0, 0.0)
        self.look_at = (0.0, 0.0, 1.0)

        self.waiting_to_respawn = False

        self.flags = 0

        self.timestamp = 0

        # Future protocol fields

        self.avatar_loadout = {}

        self.weapon_loadout = {}

        self.weapon_ammo = {}

        self.skills = {}

        self.applied_buffs = []

        self.pwn_loadout = []