import threading
import time

from gameserver.session_manager import session_manager


class GameLoop:

    TICK_RATE = 20
    DELTA = 1.0 / TICK_RATE

    def start(self):

        thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        thread.start()

    def run(self):

        while True:

            for session in session_manager.sessions.values():

                session.update(self.DELTA)

            time.sleep(self.DELTA)


game_loop = GameLoop()