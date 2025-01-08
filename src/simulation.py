from typing import List, Tuple
from .car import Car

class Simulation:
      def __init__(self, width: int, height: int):
          self.width = width
          self.height = height
          self.cars: List[Car] = []

      def add_car(self, car: Car) -> None:
          # Validate initial position
          if not (0 <= car.position.x < self.width and 
                 0 <= car.position.y < self.height):
              raise ValueError(f"Initial position ({car.position.x},{car.position.y}) "
                             f"is outside the field bounds of {self.width}x{self.height}")
          
          # Check for collision with existing cars
          for existing_car in self.cars:
              if existing_car.position == car.position:
                  raise ValueError(f"Car {car.name} would collide with {existing_car.name} "
                                 f"at initial position ({car.position.x},{car.position.y})")
          
          self.cars.append(car)

      def check_collision(self, current_car: Car) -> Tuple[bool, List[Car]]:
          """Check if current car collides with any other car"""
          collided_cars = []
          for other_car in self.cars:
              if (other_car != current_car and 
                  other_car.position == current_car.position and 
                  not other_car.collision_step):
                  collided_cars.append(other_car)
          return len(collided_cars) > 0, collided_cars

      def run(self) -> List[str]:
          max_steps = max(len(car.commands) for car in self.cars)

          for step in range(max_steps):
              # Process each car sequentially within the step
              for car in self.cars:
                  if not car.collision_step and car.has_next_command():
                      car.execute_next_command(self.width, self.height)
                      
                      # Check for collision after this car's movement
                      has_collision, collided_cars = self.check_collision(car)
                      if has_collision:
                          current_step = step + 1
                          car.collision_step = current_step
                          car.collided_with = ", ".join(sorted(other.name for other in collided_cars))
                          
                          for other_car in collided_cars:
                              other_car.collision_step = current_step
                              other_car.collided_with = car.name
                          
                          # Generate collision results
                          results = []
                          all_collided_cars = [car] + collided_cars
                          for collided_car in sorted(all_collided_cars, key=lambda x: x.name):
                              results.append(
                                  f"{collided_car.name}, collides with {collided_car.collided_with} at "
                                  f"({collided_car.position.x},{collided_car.position.y}) at step {collided_car.collision_step}"
                              )
                          return results
          
          return [
              f"{car.name}, ({car.position.x},{car.position.y}) {car.direction.value}"
              for car in sorted(self.cars, key=lambda x: x.name)
          ]