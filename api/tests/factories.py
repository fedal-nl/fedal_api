import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ("name",)

    name = "test_group"

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    password = factory.PostGenerationMethodCall("set_password", "defaultpassword")
    email = factory.Faker("email", locale="nl_NL")

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)
        else:
            # Add the user to the test_group by default
            self.groups.add(GroupFactory())

# import factories
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# from factory.django import DjangoModelFactory

# from ..aclconfig import Role

# User = get_user_model()


# class GroupFactory(DjangoModelFactory):
#     class Meta:
#         model = Group
#         django_get_or_create = ("name",)


# class UserFactory(DjangoModelFactory):
#     class Meta:
#         model = User

#     username = factory.Sequence(lambda n: "user{:d}".format(n))
#     password = factory.PostGenerationMethodCall("set_password", "defaultpassword")
#     email = factory.Faker("email", locale="nl_NL")

#     @factory.post_generation
#     def groups(self, create, extracted, **kwargs):
#         if not create:
#             return

#         if extracted:
#             for group in extracted:
#                 self.groups.add(group)


# class SuperUserFactory(UserFactory):
#     is_staff = True
#     is_superuser = True


# class AdminUserFactory(UserFactory):
#     @factory.post_generation
#     def groups(self: User, create, extracted, **kwargs):
#         if not create:
#             return
#         self.groups.add(GroupFactory(name=Role.ADMIN))
