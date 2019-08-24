import factory


class UserFactory(factory.django.DjangoModelFactory):
    factory.Sequence(lambda n: "user{0}@example.com".format(n))
    password = factory.PostGenerationMethodCall("set_password", "password")

    class Meta:
        model = "accounts.User"
        django_get_or_create = ["email"]
