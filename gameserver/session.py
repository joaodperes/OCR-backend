from gameserver.round_state import RoundState
from gameserver.bot import Bot
from gameserver.events import EventQueue
import uuid

class Session:

    TARGET_POPULATION = 8

    def __init__(self):

        self.players = {}

        self.next_player_id = 1

        self.round_state = RoundState.SETUP

        self.server_time = 0

        self.tick = 0

        self.events = EventQueue()

        self.id = uuid.uuid4()

        self.map_name = "ruaturbine"

        """ 	private void SetupLevelArrays()
            {
                this.exploreMapModeLevels = new string[11];
                this.exploreMapModeLevels[0] = "DM-Slums";
                this.exploreMapModeLevels[1] = "courtyard";
                this.exploreMapModeLevels[2] = "DM-Burninator";
                this.exploreMapModeLevels[3] = "DirtyRiver";
                this.exploreMapModeLevels[4] = "Probetown";
                this.exploreMapModeLevels[5] = "turbine";
                this.exploreMapModeLevels[6] = "firstblood";
                this.exploreMapModeLevels[7] = "IsleKillya";
                this.exploreMapModeLevels[8] = "Graveyard";
                this.exploreMapModeLevels[9] = "echelonjr";
                this.exploreMapModeLevels[10] = "DM-Ceres";
                this.annihilatorModeLevels = new string[9];
                this.annihilatorModeLevels[0] = "DM-Slums";
                this.annihilatorModeLevels[1] = "courtyard";
                this.annihilatorModeLevels[2] = "DM-Burninator";
                this.annihilatorModeLevels[3] = "DirtyRiver";
                this.annihilatorModeLevels[4] = "Probetown";
                this.annihilatorModeLevels[5] = "turbine";
                this.annihilatorModeLevels[6] = "firstblood";
                this.annihilatorModeLevels[7] = "Graveyard";
                this.annihilatorModeLevels[8] = "echelonjr";
                this.tdModeLevels = new string[2];
                this.tdModeLevels[0] = "Graveyard";
                this.tdModeLevels[1] = "DirtyRiver";
            } 
        """

        self.game_type = 0

        self.variation_id = 0

        self.session_type = 0

        self.max_players = 8

        self.allow_consumables = True

        self.force_respawn = True

    def update(self, dt):

        self.server_time += dt
        self.tick += 1

        self.ensure_population()

        for player in self.players.values():

            if isinstance(player, Bot):
                player.update(dt)

    def ensure_population(self):

        while len(self.players) < self.TARGET_POPULATION:

            self.add_player(Bot())

    def add_player(self, player):

        player.player_id = self.next_player_id

        self.next_player_id += 1

        self.players[player.player_id] = player

        print(
            f"[SESSION] Added {player.account_name} "
            f"(PlayerId={player.player_id})"
        )


        return player