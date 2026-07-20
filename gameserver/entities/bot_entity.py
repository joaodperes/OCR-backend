import random

from .player_entity import PlayerEntity


class BotEntity(PlayerEntity):

    names = [

        "Alpha",
        "Bravo",
        "Charlie",
        "Delta",
        "Echo",
        "Foxtrot",
        "Ghost",
        "Hunter",
        "Reaper",
        "Viper",
        "Falcon",
        "Wolf"

    ]

    def __init__(self):

        super().__init__()

        self.is_bot = True

        self.account_name = random.choice(self.names)

        self.ai_timer = 0.0

    def update(self, dt):

        self.ai_timer += dt