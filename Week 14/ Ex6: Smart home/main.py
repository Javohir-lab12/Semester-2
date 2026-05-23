from factory import DeviceFactory
from event_log import EventLog
from sensor import TempSensor
log = EventLog()

if __name__ == "__main__":
    sensor = TempSensor()
    heater = DeviceFactory.create('heater', 'Living room heater')
    ac = DeviceFactory.create('ac', 'Bedroom AC')
    alarm = DeviceFactory.create('alarm', 'Fire Alarm')
    sensor.attach(heater)
    sensor.attach(ac)
    sensor.attach(alarm)
    readings = [22, 16, 14, 28, 30, 45, 25]
    for temp in readings:
        sensor.report(temp)
    print(f"Total events logged: {len(log.events)}")