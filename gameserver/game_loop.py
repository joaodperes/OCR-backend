import threading
import time

from .session_manager import session_manager


class GameLoop:

    def start(self):

        thread = threading.Thread(target=self.run)

        thread.daemon = True

        thread.start()

    def run(self):

        print("Game loop started")

        previous = time.time()

        while True:

            now = time.time()

            dt = now - previous

            previous = now

            session = session_manager.get_current()

            if session is not None:

                session.update(dt)

            time.sleep(0.05)


game_loop = GameLoop()