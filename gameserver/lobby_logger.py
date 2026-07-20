from datetime import datetime


class LobbyLogger:

    @staticmethod
    def divider():

        print("=" * 70)

    @staticmethod
    def log(message):

        now = datetime.now().strftime("%H:%M:%S")

        print(f"[{now}] {message}")

    @staticmethod
    def print_session(session):

        LobbyLogger.divider()

        LobbyLogger.log(f"Session : {session.id}")
        LobbyLogger.log(f"Map     : {session.map_name}")
        LobbyLogger.log(f"Players : {len(session.players)}")
        LobbyLogger.log(f"Bots    : {len(session.bots)}")

        print()

        print("Human Players")

        if session.players:

            for player in session.players:

                print(f"  {player.account_name}")

        else:

            print("  <none>")

        print()

        print("Bots")

        if session.bots:

            for bot in session.bots:

                print(f"  {bot.account_name}")

        else:

            print("  <none>")

        LobbyLogger.divider()