from faker import Faker
from faker.providers import BaseProvider

fake = Faker("en_US")


class MobileNumberProvider(BaseProvider):
    mobile_formats = ("+49##########",)

    def mobile_number(self):
        return self.numerify(self.random_element(self.mobile_formats))


fake.add_provider(MobileNumberProvider)
