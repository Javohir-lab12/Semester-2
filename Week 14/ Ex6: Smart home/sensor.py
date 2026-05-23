from event_log import EventLog
log = EventLog()

class TempSensor:
    def __init__(self):
        self.listeners = []
    def attach(self, listener):
        self.listeners.append(listener)
    def report(self, temp):
        log.add(f"🌡️ Sensor reports {temp}°C")
        for listener in self.listeners:
            listener.on_reading(temp)