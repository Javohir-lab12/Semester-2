class Thermostat:
    min_temp = 15.0
    max_temp = 30.0
    device_count = 0
    def __init__(self, location, initial_temp):
        self.location = location
        self.initial_temp = initial_temp
        self.readings = []
        if self.initial_temp < Thermostat.min_temp:
            print("Initial temperature out of range. Set to minimum.")
            self.current_temp = Thermostat.min_temp
            print(f"Temperature set to {self.current_temp}\n")
        elif self.initial_temp > Thermostat.max_temp:
            print("Initial temperature out of range. Set to maximum.")
            self.current_temp = Thermostat.max_temp
            print(f"Temperature set to {self.current_temp}\n")
        else:
            self.current_temp = self.initial_temp
            print(f"Temperature set to {self.current_temp}°C\n")
        self.readings.append(self.current_temp)
        Thermostat.device_count += 1
    def set_temperature(self, new_temp):
        if Thermostat.min_temp <= new_temp <= Thermostat.max_temp:
            self.current_temp = float(new_temp)
            self.readings.append(self.current_temp)
            print(f"Temperature set to {self.current_temp}°C\n")
        else:
            print(f"Temperature {new_temp}°C is out of allowed range (15.0-30.0)\n")

    def get_average_temp(self):
        return float(sum(self.readings)/len(self.readings))

    def display_status(self):
        print(f"Thermostat in {self.location}: {self.current_temp}°C")
        print(f"Reading count: {len(self.readings)}")
        print(f"Average temperature: {self.get_average_temp()}°C\n")
    def is_comfortable(self):
        print(20 <= self.current_temp <= 25)

living_room = Thermostat("Living room", 22)
garage = Thermostat("Garage", 10)
living_room.set_temperature(26.5)
living_room.set_temperature(35)
living_room.display_status()
garage.display_status()
living_room.is_comfortable()
print(living_room.device_count)