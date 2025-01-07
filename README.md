# Auto Driving Car Simulation

A simulation program for autonomous driving cars that enables multiple vehicles to navigate a rectangular field while handling collisions and boundary conditions.

## 🚀 Features

- Multi-car simulation support
- Real-time collision detection
- Boundary enforcement
- Sequential command processing
- Command-line interface
- Comprehensive test coverage
- No external dependencies

## 🛠️ Requirements

- Python 3.7+
- No additional packages required


## 🚗 Quick Start

1. Clone the repository:
cd auto-driving-car-simulation

2. Run the simulation:
python3 main.py

3. Run tests:
python3 -m unittest discover tests 

## 🎮 Usage
Basic Commands:

- F: Move forward one grid point
- L: Rotate 90 degrees left
- R: Rotate 90 degrees right

Directions:

- N: North
- S: South
- E: East
- W: West

Example Session:

Welcome to Auto Driving Car Simulation!

Please enter the width and height of the simulation field in x y format:
> 10 10

Please choose from the following options:
[1] Add a car to field
[2] Run simulation
> 1

Please enter the name of the car:
> A

Please enter initial position of car A in x y Direction format:
> 1 2 N

Please enter the commands for car A:
> FFRFFFFRRL

## 🔧 Technical Details
Coordinate System
- Origin (0,0) is at the bottom-left corner
- X-axis increases towards the east
- Y-axis increases towards the north
- Field boundaries are exclusive (e.g., 10x10 field has coordinates 0-9)

Simulation Rules
- Commands are processed sequentially for all cars
- Only one command per car is executed in each step
- Cars stop moving after collision
- Moves that would go beyond boundaries are ignored
- Car names must be unique

Command Processing
Step 1: Car A moves → Car B moves
Step 2: Car A moves → Car B moves
Step 3: Car A rotates → Car B rotates
...and so on

## 🧪 Testing
Tests cover:

- Basic movement mechanics
- Rotation functionality
- Boundary condition handling
- Collision detection
- Invalid input handling
- Multi-car scenarios




