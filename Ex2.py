class Duration:
    def __init__(self, total_minutes):
        self.total_minutes = total_minutes
    def __str__(self):
        # hours, mins = divmod(self.total_minutes, 60)
        return f"{self.total_minutes // 60}h {self.total_minutes % 60}m"
    def __add__(self, duration):
        # new_duration = self.total_minutes + duration.total_minutes
        # return f"{new_duration // 60}h {new_duration % 60}m"
        return Duration(self.total_minutes + duration.total_minutes)
    def __gt__(self, duration):
        return self.total_minutes > duration.total_minutes
    def __bool__(self):
        return self.total_minutes > 0
    
d1 = Duration(90)
d2 = Duration(45)
d3 = d1 + d2
print(d1)
print(d2)
print(d3)
print(d1 > d2)
d4 = Duration(0)
if not d4:
    print("No time left")