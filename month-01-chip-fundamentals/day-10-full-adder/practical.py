"""Day 010 - A full adder from two half adders and OR."""


def check_bit(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError("Inputs must be integer 0 or 1")
    return value


def half_adder(a, b):
    a, b = check_bit(a), check_bit(b)
    return a ^ b, a & b


def full_adder(a, b, carry_in):
    a, b, carry_in = check_bit(a), check_bit(b), check_bit(carry_in)
    first_sum, first_carry = half_adder(a, b)
    sum_bit, second_carry = half_adder(first_sum, carry_in)
    carry_out = first_carry | second_carry
    return sum_bit, carry_out


def main():
    print("Chip Technology - Day 010")
    print("A B Cin | SUM Cout | RESULT")
    for a in (0, 1):
        for b in (0, 1):
            for carry_in in (0, 1):
                sum_bit, carry_out = full_adder(a, b, carry_in)
                assert sum_bit + 2 * carry_out == a + b + carry_in
                print(f"{a} {b}  {carry_in}  |  {sum_bit}    {carry_out}   |   {carry_out}{sum_bit}")

    assert full_adder(1, 1, 1) == (1, 1)
    for invalid in (-1, 2, True, "1"):
        try:
            full_adder(0, 1, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid bit accepted")

    print("All tests passed!")


if __name__ == "__main__":
    main()
