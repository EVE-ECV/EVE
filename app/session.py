"""
Session Manager

Stores temporary workflow sessions.

For Version 0.1 this is in-memory only.
Later this can be replaced by SQLite,
PostgreSQL or Redis.
"""

import uuid


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def create(self, task):
        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "task": task,
            "state": "waiting_boss_confirmation"
        }

        return session_id

    def get(self, session_id):
        return self.sessions.get(session_id)

    def update_state(self, session_id, state):
        if session_id in self.sessions:
            self.sessions[session_id]["state"] = state

    def delete(self, session_id):
        self.sessions.pop(session_id, None)
