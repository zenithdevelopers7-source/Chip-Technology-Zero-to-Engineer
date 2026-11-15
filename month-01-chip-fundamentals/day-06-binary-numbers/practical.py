"""Day 006 — Beginner binary representation exercises."""


def decimal_to_binary(value, width=8):
    """Return exactly width bits for a non-negative integer that fits."""
    if type(value) is not int or type(width) is not int:
        raise TypeError("Value and width must be integers")
    if width <= 0 or value < 0 or value >= (1 << width):
        raise ValueError("Value must fit within the positive bit width")
    return format(value, f"0{width}b")


def binary_to_decimal(bits):
    if not isinstance(bits, str) or not bits or any(c not in "01" for c in bits):
        raise ValueError("Binary input must be a non-empty string of 0s and 1s")
    return int(bits, 2)


def main():
    print("Chip Technology - Day 006")
    print("Decimal | 8-bit Binary")
    for number in [0, 1, 5, 13, 42, 255]:
        print(f"{number:>7} | {decimal_to_binary(number)}")

    assert decimal_to_binary(13) == "00001101"
    assert binary_to_decimal("00001101") == 13
    assert decimal_to_binary(255) == "11111111"
    assert binary_to_decimal("101010") == 42

    for bad in ("102", "", "apple"):
        try:
            binary_to_decimal(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid binary input was accepted")

    print("All tests passed!")


if __name__ == "__main__":
    main()
