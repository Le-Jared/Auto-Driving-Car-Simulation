from enum import Enum
from dataclasses import dataclass

class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    @classmethod
    def from_str(cls, direction: str) -> 'Direction':
        try:
            return cls(direction.upper())
        except ValueError:
            raise ValueError(f"Invalid direction: {direction}. Must be one of N, S, E, W")

    def turn_left(self) -> 'Direction':
        rotations = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH
        }
        return rotations[self]

    def turn_right(self) -> 'Direction':
        rotations = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        return rotations[self]

@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

class Car:
    def __init__(self, name: str, position: Position, direction: Direction, commands: str):
        self.name = name
        self.position = position
        self.direction = direction
        self.commands = commands
        self.command_index = 0
        self.collision_step = None
        self.collided_with = None
        
    def get_next_position(self) -> Position:
        """Calculate next position based on current direction without moving the car"""
        moves = {
            Direction.NORTH: (0, 1),
            Direction.SOUTH: (0, -1),
            Direction.EAST: (1, 0),
            Direction.WEST: (-1, 0)
        }
        dx, dy = moves[self.direction]
        return Position(self.position.x + dx, self.position.y + dy)

    def has_next_command(self) -> bool:
        return self.command_index < len(self.commands) and not self.collision_step

    def execute_next_command(self, field_width: int, field_height: int) -> None:
        if not self.has_next_command():
            return

        command = self.commands[self.command_index]
        if command == 'L':
            self.direction = self.direction.turn_left()
        elif command == 'R':
            self.direction = self.direction.turn_right()
        elif command == 'F':
            next_pos = self.get_next_position()
            if (0 <= next_pos.x < field_width and 
                0 <= next_pos.y < field_height):
                self.position = next_pos
        
        self.command_index += 1

    def __str__(self) -> str:
        return f"{self.name}, ({self.position.x},{self.position.y}) {self.direction.value}"
