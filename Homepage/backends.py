# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, login_type=None, **kwargs):
        try:
            # Retrieve the user based on the username and login_type
            user = CustomUser.objects.get(username=username, account_type=login_type)
            print("authentication passed")
            # Check the user's password
            if user.check_password(password):
                return user
            else:
                return None

        except CustomUser.DoesNotExist:
            # User does not exist
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
