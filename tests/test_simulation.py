import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.car import Car, Direction, Position
from src.simulation import Simulation

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(10, 10)

    def test_car_movement(self):
        # Test basic movement
        car = Car("A", Position(1, 1), Direction.NORTH, "FFF")
        self.simulation.add_car(car)
        self.simulation.run()
        self.assertEqual(car.position.x, 1)
        self.assertEqual(car.position.y, 4)

    def test_car_rotation(self):
        # Test rotation
        car = Car("A", Position(1, 1), Direction.NORTH, "RRL")
        self.simulation.add_car(car)
        self.simulation.run()
        self.assertEqual(car.direction, Direction.EAST)

    def test_boundary_limits(self):
        # Test boundary limits
        car = Car("A", Position(0, 0), Direction.SOUTH, "F")
        self.simulation.add_car(car)
        self.simulation.run()
        self.assertEqual(car.position.y, 0)  # Should not move south

    def test_collision_detection(self):
        # Test collision between cars
        car1 = Car("A", Position(1, 1), Direction.EAST, "FF")
        car2 = Car("B", Position(3, 1), Direction.WEST, "FF")
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        results = self.simulation.run()
        
        # Both cars should have collision_step set
        self.assertIsNotNone(car1.collision_step)
        self.assertIsNotNone(car2.collision_step)
        
        # Check if collision is reported in results
        self.assertTrue(any("collides" in result for result in results))

    def test_invalid_initial_position(self):
        # Test adding car outside field bounds
        with self.assertRaises(ValueError):
            car = Car("A", Position(11, 11), Direction.NORTH, "F")
            self.simulation.add_car(car)

    def test_invalid_direction(self):
        # Test invalid direction
        with self.assertRaises(ValueError):
            Direction.from_str("X")

if __name__ == '__main__':
    unittest.main()
