"""Day 007 — AND, OR, and NOT digital logic gates."""


def check_bit(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError("Inputs must be integer 0 or 1")
    return value


def and_gate(a, b):
    return check_bit(a) & check_bit(b)


def or_gate(a, b):
    return check_bit(a) | check_bit(b)


def not_gate(a):
    return 1 - check_bit(a)


def main():
    print("Chip Technology - Day 007")
    print("A B | AND OR")
    for a in (0, 1):
        for b in (0, 1):
            print(f"{a} {b} |  {and_gate(a,b)}   {or_gate(a,b)}")

    print("\nA | NOT")
    for a in (0, 1):
        print(f"{a} |  {not_gate(a)}")

    assert [and_gate(a, b) for a in (0, 1) for b in (0, 1)] == [0, 0, 0, 1]
    assert [or_gate(a, b) for a in (0, 1) for b in (0, 1)] == [0, 1, 1, 1]
    assert [not_gate(a) for a in (0, 1)] == [1, 0]

    for invalid in (-1, 2, "1", True):
        try:
            and_gate(invalid, 1)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid input was accepted")

    print("All tests passed!")


if __name__ == "__main__":
    main()
