import uuid
from enum import Enum

from gameserver.entities.player_entity import PlayerEntity
from gameserver.entities.bot_entity import BotEntity


class RoundState(Enum):
    SETUP = 0
    RUNNING = 1
    FINISHED = 2


class Session:

    def __init__(self):

        # Unique session identifier
        self.id = uuid.uuid4()

        # Session settings
        self.session_type = 0
        self.game_type = 0
        self.variation_id = 0

        # Map
        self.map_name = "ruaturbine"

        # Player limits
        self.max_players = 8
        self.max_spectators = 4

        # Gameplay options
        self.allow_consumables = True
        self.force_respawn = True

        # Connected entities
        self.players = {}
        self.bots = {}
        self.spectators = {}

        # Match state
        self.round_state = RoundState.SETUP

        self.match_time = 0.0
        self.setup_time = 10.0

        # Bot settings
        self.minimum_population = 8
        self.next_bot_id = 1000

    # ----------------------------------------------------
    # Player Management
    # ----------------------------------------------------

    def add_player(self, player):

        self.players[player.player_id] = player

        print(f"[SESSION] Player joined: {player.name}")

    def remove_player(self, player_id):

        if player_id in self.players:

            print(f"[SESSION] Player left: {player_id}")

            del self.players[player_id]

    # ----------------------------------------------------
    # Bot Management
    # ----------------------------------------------------

    def add_bot(self):

        bot = BotEntity()

        bot.player_id = self.next_bot_id
        bot.name = f"Bot {bot.player_id}"

        self.next_bot_id += 1

        self.bots[bot.player_id] = bot

        print(f"[SESSION] Added {bot.name}")

        return bot

    def remove_bot(self, player_id):

        if player_id in self.bots:

            print(f"[SESSION] Removed bot {player_id}")

            del self.bots[player_id]

    # ----------------------------------------------------
    # Population
    # ----------------------------------------------------

    def ensure_population(self):

        total = len(self.players) + len(self.bots)

        while total < self.minimum_population:

            self.add_bot()

            total += 1

    # ----------------------------------------------------
    # Match Update
    # ----------------------------------------------------

    def update(self, dt):

        self.match_time += dt

        self.ensure_population()

        if self.round_state == RoundState.SETUP:

            if self.match_time >= self.setup_time:

                self.round_state = RoundState.RUNNING

                print("[SESSION] Match started")

        elif self.round_state == RoundState.RUNNING:

            for bot in self.bots.values():

                bot.update(dt)

    # ----------------------------------------------------
    # Helpers
    # ----------------------------------------------------

    @property
    def num_players(self):

        return len(self.players) + len(self.bots)

    @property
    def num_connections(self):

        return len(self.players)

    @property
    def num_spectators(self):

        return len(self.spectators)

    def get_all_players(self):

        for player in self.players.values():
            yield player

        for bot in self.bots.values():
            yield bot