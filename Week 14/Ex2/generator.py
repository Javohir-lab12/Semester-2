class IDGenerator:
    _instanse = None
    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
            cls._instanse.current = 0
        return cls._instanse
    def next_id(self):
        self.current += 1
        return self.current