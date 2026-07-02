from gameserver.player import Player


class PlayerManager:

    def __init__(self):

        self.players = {}

        self.next_id = 1

    def create_player(self, account):

        player = Player()

        player.player_id = self.next_id
        self.next_id += 1

        player.account_id = account["Id"]
        player.account_name = account["AccountName"]

        self.players[player.player_id] = player

        return player


player_manager = PlayerManager()