"""Day 005 - Idealized NMOS pull-down circuit.

Educational digital model, not a physical transistor simulator.
"""


def nmos_on(gate):
    if type(gate) is not int or gate not in (0, 1):
        raise ValueError("Gate must be the integer 0 or 1")
    return gate == 1


def output_level(gate):
    """Pull-up yields HIGH when NMOS off; NMOS pulls LOW when on."""
    return 0 if nmos_on(gate) else 1


def main():
    print("Chip Technology - Day 005")
    print("Gate | NMOS | Output")
    for gate in (0, 1):
        state = "ON" if nmos_on(gate) else "OFF"
        print(f"  {gate}  | {state:<4} |   {output_level(gate)}")

    assert output_level(0) == 1
    assert output_level(1) == 0

    try:
        output_level(2)
    except ValueError:
        print("Invalid gate signal correctly rejected")
    else:
        raise AssertionError("Expected invalid gate signal error")

    print("All tests passed!")


if __name__ == "__main__":
    main()
