"""Day 002 - Ohm's Law Calculator."""

def calculate_current(voltage, resistance):
    if resistance <= 0:
        raise ValueError("Resistance must be positive")
    return voltage / resistance


def main():
    voltage = 5.0
    resistance = 1000.0

    current = calculate_current(voltage, resistance)

    print("Chip Technology - Day 002")
    print(f"Voltage: {voltage} V")
    print(f"Resistance: {resistance} ohms")
    print(f"Current: {current:.3f} A")
    print(f"Current: {current * 1000:.2f} mA")

    assert current == 0.005


if __name__ == "__main__":
    main()
