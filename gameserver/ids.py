class IdGenerator:

    def __init__(self):

        self.next_player = 1

    def next_player_id(self):

        pid = self.next_player

        self.next_player += 1

        return pid