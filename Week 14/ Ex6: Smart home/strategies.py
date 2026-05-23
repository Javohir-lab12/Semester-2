from abc import ABC, abstractmethod

class DeviceStrategy(ABC):
    @abstractmethod
    def evaluate(self, temp): ...

class HeaterStrategy(DeviceStrategy):
    def __init__(self, threshold):
        self.threshold = threshold
    def evaluate(self, temp):
        return 'ON' if temp < self.threshold else 'OFF'
    
class ACStrategy(DeviceStrategy):
    def __init__(self, threshold):
        self.threshold = threshold
    def evaluate(self, temp):
        return 'ON' if temp > self.threshold else 'OFF'
    
class AlarmsStrategy(DeviceStrategy):
    def evaluate(self, temp):
        return 'ALERT' if temp > 40 or temp < 0 else 'OFF'