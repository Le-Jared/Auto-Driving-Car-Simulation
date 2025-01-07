from src.simulator_cli import SimulatorCLI

def main():
    try:
        simulator = SimulatorCLI()
        simulator.start()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    main()