from faker import Faker


class NameGenerator:
    def __init__(self, faker: Faker):
        self.faker: Faker = faker

    def get_name(self, gender):
        match gender:
            case "male":
                return f"{self.faker.first_name_male()} {self.faker.last_name_male()}"
            case "female":
                return (
                    f"{self.faker.first_name_female()} {self.faker.last_name_female()}"
                )
            case _:
                raise ValueError("Invalid value provided for argument: 'gender'.")
