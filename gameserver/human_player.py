from .entities.player_entity import PlayerEntity


class HumanPlayer(PlayerEntity):

    def __init__(self):

        super().__init__()

        self.connection = None

        self.token = None

        self.authenticated = False