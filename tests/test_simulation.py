import unittest
from src.car import Car, Direction, Position
from src.simulation import Simulation

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(10, 10)

    def test_car_basic_movement(self):
        """Test basic movement in all directions"""
        test_cases = [
            (Position(5, 5), Direction.NORTH, "F", Position(5, 6), Direction.NORTH),
            (Position(5, 5), Direction.SOUTH, "F", Position(5, 4), Direction.SOUTH),
            (Position(5, 5), Direction.EAST, "F", Position(6, 5), Direction.EAST),
            (Position(5, 5), Direction.WEST, "F", Position(4, 5), Direction.WEST),
        ]

        for init_pos, init_dir, commands, exp_pos, exp_dir in test_cases:
            with self.subTest(init_pos=init_pos, init_dir=init_dir):
                simulation = Simulation(10, 10)
                car = Car("Test", init_pos, init_dir, commands)
                simulation.add_car(car)
                simulation.run()
                self.assertEqual(car.position, exp_pos)
                self.assertEqual(car.direction, exp_dir)

    def test_complex_movement_patterns(self):
        """Test more complex movement patterns"""
        test_cases = [
            # Square movement pattern
            (Position(2, 2), Direction.NORTH, "FRFRFRF", Position(2, 2), Direction.WEST),
            # Zigzag pattern
            (Position(2, 2), Direction.NORTH, "FRFLFRFL", Position(4, 4), Direction.NORTH),
            # Corrected pattern with proper final direction
            (Position(3, 3), Direction.NORTH, "FFLFFRF", Position(1, 6), Direction.NORTH),
        ]

        for init_pos, init_dir, commands, exp_pos, exp_dir in test_cases:
            with self.subTest(commands=commands):
                simulation = Simulation(10, 10)
                car = Car("Test", init_pos, init_dir, commands)
                simulation.add_car(car)
                simulation.run()
                self.assertEqual(car.position, exp_pos)
                self.assertEqual(car.direction, exp_dir)


    def test_boundary_conditions(self):
        """Test behavior at field boundaries"""
        test_cases = [
            # Try to move beyond north boundary
            (Position(5, 9), Direction.NORTH, "F", Position(5, 9)),
            # Try to move beyond south boundary
            (Position(5, 0), Direction.SOUTH, "F", Position(5, 0)),
            # Try to move beyond east boundary
            (Position(9, 5), Direction.EAST, "F", Position(9, 5)),
            # Try to move beyond west boundary
            (Position(0, 5), Direction.WEST, "F", Position(0, 5)),
        ]

        for init_pos, direction, commands, exp_pos in test_cases:
            with self.subTest(init_pos=init_pos, direction=direction):
                simulation = Simulation(10, 10)
                car = Car("Test", init_pos, direction, commands)
                simulation.add_car(car)
                simulation.run()
                self.assertEqual(car.position, exp_pos)

    def test_multiple_car_interactions(self):
        """Test interactions between multiple cars"""
        # Test parallel movement without collision
        simulation1 = Simulation(10, 10)
        car1 = Car("A", Position(1, 1), Direction.NORTH, "FF")
        car2 = Car("B", Position(3, 1), Direction.NORTH, "FF")
        simulation1.add_car(car1)
        simulation1.add_car(car2)
        results = simulation1.run()
        self.assertIsNone(car1.collision_step)
        self.assertIsNone(car2.collision_step)

        # Test collision at intersection point
        simulation2 = Simulation(10, 10)
        car3 = Car("C", Position(2, 1), Direction.NORTH, "F")
        car4 = Car("D", Position(1, 2), Direction.EAST, "F")
        simulation2.add_car(car3)
        simulation2.add_car(car4)
        results = simulation2.run()
        self.assertEqual(car3.position, car4.position)  
        self.assertIsNotNone(car3.collision_step)
        self.assertIsNotNone(car4.collision_step)

    def test_direction_conversions(self):
        """Test direction string conversions"""
        test_cases = [
            ("N", Direction.NORTH),
            ("S", Direction.SOUTH),
            ("E", Direction.EAST),
            ("W", Direction.WEST),
            ("n", Direction.NORTH),
            ("s", Direction.SOUTH),
            ("e", Direction.EAST),
            ("w", Direction.WEST),
        ]

        for dir_str, expected_dir in test_cases:
            with self.subTest(dir_str=dir_str):
                self.assertEqual(Direction.from_str(dir_str), expected_dir)

    def test_invalid_inputs(self):
        """Test various invalid input scenarios"""
        # Test invalid direction
        with self.assertRaises(ValueError):
            Direction.from_str("X")

        # Test invalid initial position
        with self.assertRaises(ValueError):
            car = Car("Test", Position(-1, 5), Direction.NORTH, "F")
            self.simulation.add_car(car)

        # Test overlapping initial positions
        car1 = Car("A", Position(5, 5), Direction.NORTH, "F")
        car2 = Car("B", Position(5, 5), Direction.SOUTH, "F")
        self.simulation.add_car(car1)
        with self.assertRaises(ValueError):
            self.simulation.add_car(car2)

    def test_rotation_sequences(self):
        """Test complex rotation sequences"""
        test_cases = [
            ("RRRR", Direction.NORTH, Direction.NORTH),
            ("LLLL", Direction.NORTH, Direction.NORTH),
            ("RLRL", Direction.NORTH, Direction.NORTH),
            ("RRR", Direction.NORTH, Direction.WEST),
        ]

        for commands, start_dir, expected_dir in test_cases:
            with self.subTest(commands=commands):
                simulation = Simulation(10, 10)  
                car = Car("Test", Position(5, 5), start_dir, commands)
                simulation.add_car(car)
                simulation.run()
                self.assertEqual(car.direction, expected_dir)

    def test_empty_commands(self):
        """Test behavior with empty command string"""
        car = Car("Test", Position(5, 5), Direction.NORTH, "")
        self.simulation.add_car(car)
        results = self.simulation.run()
        self.assertEqual(len(results), 1)
        self.assertEqual(car.position, Position(5, 5))
        self.assertEqual(car.direction, Direction.NORTH)

if __name__ == '__main__':
    unittest.main()
