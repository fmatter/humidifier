def test_unique(humidify):
    assert humidify("dog") == "dog"
    assert humidify("dog", unique=True) == "dog-1"
    assert humidify("dog", unique=True) == "dog-2"
    assert humidify("dog", unique=True) == "dog-3"
    assert humidify("dog") == "dog-3"


def test_ascii(humidify):
    assert humidify("dög") == "dog"
    assert humidify("dög") == "dog"
    assert humidify("dog") == "dog-1"


def test_zero(humidify):
    assert humidify("", unique=True) == "null"
    assert humidify("", unique=True) == "null-1"
    assert humidify("", unique=True) == "null-2"
    assert humidify("") == "null-2"


def test_keys(humidify):
    assert humidify("dog", unique=True) != humidify("dog", unique=True)
    assert humidify("dog", "animals", unique=True) == humidify(
        "dog", "canis", unique=True
    )
    assert humidify("dog", "animals", unique=True) == humidify(
        "dog", "canis", unique=True
    )
    humidify("dog", "canis", unique=True)
    assert humidify("dog", "animals", unique=True) != humidify(
        "dog", "canis", unique=True
    )


def test_values():
    from humidifier import humidify, get_values

    humidify("dog", key="animals")
    humidify("hündchen", key="animals")
    humidify("coffee", key="drinks")
    values = get_values("animals")
    assert "dog" in values.values()
    assert "hundchen" in values.values()
    assert "coffee" not in values.values()


def test_existing():
    from humidifier import Humidifier

    hum = Humidifier(["dog"])
    assert hum.humidify("dog") == "dog-1"

    hum2 = Humidifier({"omnivores": ["dog"]})
    assert hum2.humidify("dog") == "dog"
    assert hum2.humidify("dog", "omnivores") == "dog-1"


def test_import():
    from humidifier import humidify

    assert humidify("dog") == "dog"
    assert humidify("dog", unique=True) == "dog-1"
