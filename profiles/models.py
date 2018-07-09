from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    # Using the default User Model and nothing more but this will allow us to add further attributes to the user model
    # without the need to rewrite the entire project (an AUTH_USER_MODEL class cannot be used unless it has been created
    # in the 0001 migration of its app)
    pass
