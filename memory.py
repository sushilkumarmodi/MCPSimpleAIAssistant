class Memory:
    def __init__(self):
        self.History = []

    def add(self, user, assistant):
        self.History.append({"user": user, "assistant" : assistant})

    def get_recent(self, limit = 3):
        return self.History[-limit:]