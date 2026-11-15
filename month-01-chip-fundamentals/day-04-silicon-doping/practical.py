"""Day 004 - Educational Silicon Doping Model."""

DOPANTS = {
    "phosphorus": ("N-type", "electrons"),
    "arsenic": ("N-type", "electrons"),
    "boron": ("P-type", "holes"),
    "antimony": ("N-type", "electrons"),
}


def describe_silicon(dopant=None):
    if dopant is None:
        return ("Intrinsic", "electrons and holes")

    if not isinstance(dopant, str):
        raise TypeError("Dopant must be text or None")

    name = dopant.strip().lower()

    if name not in DOPANTS:
        raise ValueError("Unknown dopant")

    return DOPANTS[name]


def main():
    print("Chip Technology - Day 004")
    print("-------------------------")

    for dopant in [None, "Phosphorus", "Boron"]:
        kind, carriers = describe_silicon(dopant)
        name = dopant if dopant is not None else "None"
        print(f"Dopant: {name}")
        print(f"Type: {kind}")
        print(f"Carriers: {carriers}")
        print()

    assert describe_silicon()[0] == "Intrinsic"
    assert describe_silicon("phosphorus")[0] == "N-type"
    assert describe_silicon("boron")[0] == "P-type"
    assert describe_silicon("arsenic")[1] == "electrons"

    assert describe_silicon("antimony")[0] == "N-type"

    print("All tests passed!")


if __name__ == "__main__":
    main()
