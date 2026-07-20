import uuid


class PlayerEntity:

    def __init__(self):

        # Identity
        self.player_id = 0
        self.account_id = uuid.uuid4()

        self.account_name = "Unknown"

        self.is_bot = False

        # Gameplay

        self.team = 0

        self.health = 100
        self.full_health = 100
        self.armor = 100

        self.flags = 0

        self.current_weapon_slot = 0

        self.waiting_to_respawn = False

        # Transform

        self.position = (0.0, 0.0, 0.0)

        self.look_at = (0.0, 0.0, 1.0)

        # Networking

        self.timestamp = 0

        # Inventory

        self.avatar_loadout = None

        self.weapon_loadout = None

        self.weapon_ammo = None

        self.skills = None

        self.applied_buffs = []

        self.pwn_loadout = []

    def update(self, dt):
        pass