from abc import ABC, abstractmethod
from event_log import EventLog
log = EventLog()

class Listener(ABC):
    @abstractmethod
    def on_reading(self, temp): ...

class Device(Listener):
    def __init__(self, name, startegy: Star):
        self.name = name
        self.startegy = startegy
        self.last_action = 'OFF'
    def on_reading(self, temp):
        action = self.startegy.evaluate(temp)
        if action == None or action == self.last_action:
            pass
        self.last_action = action
        log.add(f"{self.name} -> {action}")
        