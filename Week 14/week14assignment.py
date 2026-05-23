class BlockBox:
    _signals = None
    def __new__(cls):
        if cls._signals == None:
            cls._signals = super().__new__(cls)
            cls._signals = []
        return cls._signals
    def store(self, text):
        self._signals.append(text)
        print(f">>> {text}")