from .session import SessionManager

class GameServer:

    def __init__(self):

        self.sessions = SessionManager()

    def startup(self):
        print("[GameServer] Started")

    def shutdown(self):
        print("[GameServer] Stopped")