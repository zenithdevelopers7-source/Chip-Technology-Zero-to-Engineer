"""
Day 001: Introduction to Digital Switching

This is a simplified software model of a digital switch.
It is not a physical transistor simulation.
"""

def digital_switch(signal):
    if signal not in (0, 1):
        raise ValueError("Signal must be 0 or 1")

    if signal == 1:
        return "ON"
    return "OFF"


def main():
    print("Chip Technology - Day 001")
    print("-------------------------")

    for signal in [0, 1]:
        print(f"Input: {signal} -> Switch: {digital_switch(signal)}")


if __name__ == "__main__":
    main()
