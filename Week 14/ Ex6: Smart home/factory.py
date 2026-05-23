from strategies import HeaterStrategy, ACStrategy, AlarmsStrategy

class DeviceFactory:
    _builders = {}
    @classmethod
    def register(cls, kind):
        def decorator(function):
            cls._builders[kind] = function
            return function
        return decorator
    @classmethod
    def create(cls, kind, name):
        if kind not in cls._builders:
            raise ValueError("Unknown device: {kind}")
        return cls._builders[kind](name)
    
@DeviceFactory.register('heater')
def build_alarm(name):
    return DeviceFactory(name, HeaterStrategy(threshold=18))

@DeviceFactory.register('ac')
def build_alarm(name):
    return DeviceFactory(name, ACStrategy(threshold=26))

@DeviceFactory.register('alarm')
def build_alarm(name):
    return DeviceFactory(name, AlarmsStrategy())