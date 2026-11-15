"""Day 008 - Boolean NAND, NOR, XOR and XNOR gates."""


def bit(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError("Each input must be the integer 0 or 1")
    return value


def nand_gate(a, b):
    return 1 - (bit(a) & bit(b))


def nor_gate(a, b):
    return 1 - (bit(a) | bit(b))


def xor_gate(a, b):
    return bit(a) ^ bit(b)


def xnor_gate(a, b):
    return 1 - xor_gate(a, b)


def main():
    print("Chip Technology - Day 008")
    print("A B | NAND NOR XOR XNOR")
    expected = [
        (0, 0, 1, 1, 0, 1),
        (0, 1, 1, 0, 1, 0),
        (1, 0, 1, 0, 1, 0),
        (1, 1, 0, 0, 0, 1),
    ]

    for a, b, nand, nor, xor, xnor in expected:
        got = (nand_gate(a, b), nor_gate(a, b),
               xor_gate(a, b), xnor_gate(a, b))
        assert got == (nand, nor, xor, xnor)
        print(f"{a} {b} |   {got[0]}    {got[1]}   {got[2]}    {got[3]}")

    for invalid in (2, -1, True, "1"):
        try:
            xor_gate(invalid, 0)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid bit was accepted")

    print("All tests passed!")


if __name__ == "__main__":
    main()
