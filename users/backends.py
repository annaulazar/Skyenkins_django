from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None
