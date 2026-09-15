from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,brand : str, model : str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        """ Abstract method : start engine - all concrete subclasses must implement this method """
        pass

    @abstractmethod
    def drive(self):
        """Abstract method : drive - all concrete subclasses must implement this method"""
        pass

    @abstractmethod
    def shift_gears(self):
        """Abstract method : shift gears - all concrete subclasses must implement this method"""
        pass


class SportsCar(Car):
    def __init__(self, brand, model , turbo_boost : bool = True):
        super().__init__(brand, model)
        self.turbo_boost = turbo_boost
        self.current_gear = 1

    def start_engine(self):
        print(f"[{self.brand} {self.model}] V8 Engine roaring to life with rumble exhaust!")

    def drive(self):
        print(f"[{self.brand} {self.model}] Accelerating rapidly on sports suspension.")

    def shift_gears(self,gear):
        self.current_gear = gear
        print(f"[{self.brand} {self.model}] Shifted manual clutch to gear {gear}.")


class ElectricCar(Car):
    def __init__(self, brand, model , battery_capacity : float):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print(f"[{self.brand} {self.model}] System initialized silently. Ready to drive.")

    def drive(self):
        print(f"[{self.brand} {self.model}] Cruising smoothly with instant electric torque.")

    def shift_gears(self,gear):
        print(f"[{self.brand} {self.model}] Single-speed direct drive. No manual gears needed.")


if __name__ == '__main__':

    ferrari: Car = SportsCar("Ferrari", "F8 Tributo")
    tesla: Car = ElectricCar("Tesla", "Model S Plaid", battery_capacity=100.0)


    print("Testing Ferrari:")
    ferrari.start_engine()
    ferrari.drive()
    ferrari.shift_gears(3)

    print("Testing Tesla:")
    tesla.start_engine()
    tesla.drive()
    tesla.shift_gears(3)