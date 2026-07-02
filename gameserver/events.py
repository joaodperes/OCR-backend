class EventQueue:

    def __init__(self):

        self.events = []

    def push(self, event):

        self.events.append(event)

    def pop_all(self):

        events = self.events

        self.events = []

        return events