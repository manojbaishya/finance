import pytest
from faker import Faker
from faker.providers.person import Provider

from finance.sample import NameGenerator


def test_get_name(monkeypatch):

    class MockFaker:
        def first_name_male(self):
            return "John"

        def last_name_male(self):
            return "Doe"

        def first_name_female(self):
            return "Joanna"

        def last_name_female(self):
            return "Taylor"

    mock_faker = MockFaker()

    monkeypatch.setattr(Provider, "first_name_male", mock_faker.first_name_male)
    monkeypatch.setattr(Provider, "last_name_male", mock_faker.last_name_male)
    monkeypatch.setattr(Provider, "first_name_female", mock_faker.first_name_female)
    monkeypatch.setattr(Provider, "last_name_female", mock_faker.last_name_female)

    name_generator = NameGenerator(Faker())

    male_name = name_generator.get_name("male")
    assert male_name == "John Doe"

    female_name = name_generator.get_name("female")
    assert female_name == "Joanna Taylor"

    with pytest.raises(ValueError):
        name_generator.get_name("unknown")
