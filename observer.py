class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def register(self, observer):
        self.observers.append(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature)


class DisplayDevice:
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} Display: Temperature = {temperature}°C")


# Create weather station
station = WeatherStation()

# Create display devices
mobile = DisplayDevice("Mobile")
laptop = DisplayDevice("Laptop")
tv = DisplayDevice("TV")

# Register devices
station.register(mobile)
station.register(laptop)
station.register(tv)

# Change temperature
station.set_temperature(30.5)
station.set_temperature(35.2)