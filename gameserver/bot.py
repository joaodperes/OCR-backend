from gameserver.player import Player


class Bot(Player):

    counter = 1

    def __init__(self):

        super().__init__()

        self.account_name = f"BOT {Bot.counter}"

        Bot.counter += 1

    def update(self, dt):

        self.timestamp += int(dt * 1000)