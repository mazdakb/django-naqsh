import factory
from factory import fuzzy


class UserFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda n: "user{0}@example.com".format(n))
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_verified = fuzzy.FuzzyChoice([True, False])

    class Meta:
        model = "accounts.User"
        django_get_or_create = ["email"]
