class EventLog:
    _instanse = None
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
            cls._instanse.events = []
        return cls._instanse
    def add(self, msg):
        self.events.append(msg)
        print(f"📝 {msg}")