"""Educational 2-element signed INT8 dot product. Python 3 standard library only."""
import random

MIN_I8, MAX_I8 = -128, 127


def check_int8(value):
    if type(value) is not int or not (MIN_I8 <= value <= MAX_I8):
        raise ValueError("Input must be an integer in signed INT8 range [-128, 127]")
    return value


def dot2(a, b):
    """Golden arithmetic: signed 8-bit products, 32-bit result."""
    if len(a) != 2 or len(b) != 2:
        raise ValueError("Each input vector must have exactly two elements")
    return sum(check_int8(x) * check_int8(y) for x, y in zip(a, b))


def sequential_mac(a, b):
    """Behavioral model of two MAC cycles, no physical clock simulation."""
    if len(a) != 2 or len(b) != 2:
        raise ValueError("Each vector must have exactly two elements")
    acc = 0
    trace = []
    for index, (x, y) in enumerate(zip(a, b)):
        acc += check_int8(x) * check_int8(y)
        trace.append((index, acc))
    return acc, trace


def run_tests():
    examples = [
        ((2, -3), (4, 5), -7),
        ((127, 127), (127, 127), 32258),
        ((-128, -128), (-128, -128), 32768),
        ((0, 0), (5, -8), 0),
        ((-128, 127), (127, -128), -32512),
        ((1, 2), (3, 4), 11),
    ]
    for a, b, expected in examples:
        assert dot2(a, b) == expected
        actual, trace = sequential_mac(a, b)
        assert actual == expected and len(trace) == 2

    rng = random.Random(1101)
    for _ in range(2000):
        a = tuple(rng.randint(-128, 127) for _ in range(2))
        b = tuple(rng.randint(-128, 127) for _ in range(2))
        expected = a[0] * b[0] + a[1] * b[1]
        assert dot2(a, b) == expected
        assert sequential_mac(a, b)[0] == expected

    for bad in [-129, 128, True, "8", 3.5]:
        try:
            dot2((bad, 1), (1, 1))
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid INT8 operand accepted")

    print("Example: [2, -3] dot [4, 5] =", dot2((2, -3), (4, 5)))
    print("Golden reference checked: 6 edge vectors + 2,000 random vectors")
    print("All software reference tests passed!")


if __name__ == "__main__":
    run_tests()
