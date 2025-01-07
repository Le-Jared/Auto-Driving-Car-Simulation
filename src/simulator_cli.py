from .car import Car, Direction, Position
from .simulation import Simulation

class SimulatorCLI:
    def __init__(self):
        self.simulation = None

    def start(self):
        print("Welcome to Auto Driving Car Simulation!\n")
        while True:
            try:
                self._create_field()
                self._main_loop()
            except KeyboardInterrupt:
                print("\nSimulation interrupted.")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue

    def _create_field(self):
        while True:
            try:
                print("Please enter the width and height of the simulation field in x y format:")
                width, height = map(int, input().strip().split())
                if width <= 0 or height <= 0:
                    raise ValueError("Width and height must be positive numbers")
                self.simulation = Simulation(width, height)
                print(f"\nYou have created a field of {width} x {height}.")
                break
            except ValueError as e:
                print(f"Error: {e}")

    def _add_car(self):
        try:
            print("\nPlease enter the name of the car:")
            name = input().strip()
            
            print(f"Please enter initial position of car {name} in x y Direction format:")
            x, y, direction_str = input().strip().split()
            position = Position(int(x), int(y))
            direction = Direction.from_str(direction_str)
            
            print(f"Please enter the commands for car {name}:")
            commands = input().strip().upper()
            if not all(c in 'LRF' for c in commands):
                raise ValueError("Commands must only contain L, R, or F")
            
            car = Car(name, position, direction, commands)
            self.simulation.add_car(car)
            
        except ValueError as e:
            print(f"Error: {e}")
            return False
        return True

    def _display_cars(self):
        print("\nYour current list of cars are:")
        for car in self.simulation.cars:
            print(f"- {car}, {car.commands}")

    def _main_loop(self):
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            
            choice = input().strip()
            
            if choice == '1':
                self._add_car()
                self._display_cars()
            elif choice == '2':
                if not self.simulation.cars:
                    print("Error: No cars added to the simulation")
                    continue
                
                self._display_cars()
                results = self.simulation.run()
                
                print("\nAfter simulation, the result is:")
                for result in results:
                    print(f"- {result}")
                
                print("\nPlease choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")
                
                choice = input().strip()
                if choice == '1':
                    break
                elif choice == '2':
                    print("\nThank you for running the simulation. Goodbye!")
                    exit(0)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    simulator = SimulatorCLI()
    simulator.start()