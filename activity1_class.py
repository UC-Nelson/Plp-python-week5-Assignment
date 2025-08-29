class Car:
    def __init__(self, brand, model, year, fuel):
        
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.is_started = False

   
    def start(self):
        if not self.is_started:
            self.is_started = True
            print(f"{self.brand} {self.model} ({self.year}) is now started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_started:
            self.is_started = False
            print(f"{self.brand} {self.model} is now turned off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def refuel(self, amount):
        self.fuel += amount
        if self.fuel > 100:
            self.fuel = 100
        print(f"{self.brand} {self.model} refueled. Fuel level: {self.fuel}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) | Fuel: {self.fuel}%"


class BMW(Car):
    def __init__(self, model, year, fuel, drive_mode):
      
        super().__init__("BMW", model, year, fuel)
        self.drive_mode = drive_mode 

  
    def start(self):
        super().start()
        if self.is_started:
            print(f"{self.brand} {self.model} is ready in {self.drive_mode} mode!")

    def activate_cruise_control(self, speed):
        if self.is_started:
            print(f"Cruise control activated at {speed} km/h on {self.brand} {self.model}.")
        else:
            print("Start the car first to use cruise control!")


car1 = Car("Toyota", "Corolla", 2020, 50)
bmw1 = BMW("M5 Competition", 2023, 80, "Sport")

print(car1)
car1.start()
car1.refuel(30)
car1.stop()

print("\n--- BMW Example ---")
print(bmw1)
bmw1.start()
bmw1.activate_cruise_control(120)
bmw1.refuel(15)
bmw1.stop()
