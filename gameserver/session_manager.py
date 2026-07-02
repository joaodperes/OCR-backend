import uuid

from .session import Session


class SessionManager:

    def __init__(self):

        self.sessions = {}

        self.current_session = None

    def create_session(self):

        session = Session()

        self.sessions[session.id] = session

        self.current_session = session

        return session

    def get_current(self):

        return self.current_session

    def get(self, session_id):

        return self.sessions.get(session_id)
    
session_manager = SessionManager()