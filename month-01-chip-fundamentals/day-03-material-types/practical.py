"""Day 003 - Electrical Material Classification."""

MATERIALS = {
    "copper": "conductor",
    "aluminum": "conductor",
    "silver": "conductor",
    "rubber": "insulator",
    "glass": "insulator",
    "plastic": "insulator",
    "silicon": "semiconductor",
    "germanium": "semiconductor",
    "gallium arsenide": "semiconductor",
}


def classify_material(name):
    if not isinstance(name, str):
        raise TypeError("Material name must be text")

    return MATERIALS.get(name.strip().lower(), "unknown")


def main():
    print("Chip Technology - Day 003")
    print("-------------------------")

    for material in ["Copper", "Rubber", "Silicon", "Glass"]:
        category = classify_material(material)
        print(f"{material}: {category}")

    assert classify_material("Copper") == "conductor"
    assert classify_material("Rubber") == "insulator"
    assert classify_material("Silicon") == "semiconductor"
    assert classify_material("Unlisted") == "unknown"

    print("All tests passed!")


if __name__ == "__main__":
    main()
