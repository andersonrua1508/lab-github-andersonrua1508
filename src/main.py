import sys
from src.greeter import greet


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <name> [hour]")
        sys.exit(1)

    name = sys.argv[1]

    if len(sys.argv) >= 3:
        try:
            hour = int(sys.argv[2])
        except ValueError:
            print("Hour must be an integer")
            sys.exit(1)
        print(greet(name, hour))
    else:
        print(greet(name))


if __name__ == "__main__":
    main()