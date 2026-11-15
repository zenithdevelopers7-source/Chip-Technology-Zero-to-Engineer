"""Day 009 — One-bit half adder built using XOR and AND."""


def check_bit(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError("Input must be integer 0 or 1")
    return value


def half_adder(a, b):
    """Return (sum_bit, carry_bit)."""
    a, b = check_bit(a), check_bit(b)
    return (a ^ b, a & b)


def main():
    print("Chip Technology - Day 009")
    print("A B | SUM CARRY | RESULT")
    expected = [(0, 0, 0, 0), (0, 1, 1, 0),
                (1, 0, 1, 0), (1, 1, 0, 1)]

    for a, b, want_sum, want_carry in expected:
        sum_bit, carry = half_adder(a, b)
        assert (sum_bit, carry) == (want_sum, want_carry)
        assert 2 * carry + sum_bit == a + b
        print(f"{a} {b} |  {sum_bit}     {carry}   |   {carry}{sum_bit}")

    for invalid in (-1, 2, True, "1"):
        try:
            half_adder(invalid, 1)
        except ValueError:
            pass
        else:
            raise AssertionError("An invalid input was accepted")

    print("All tests passed!")


if __name__ == "__main__":
    main()
