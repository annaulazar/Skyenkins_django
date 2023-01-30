# from django.contrib.auth.models import BaseUserManager
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, username, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         username = username.lower()
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, username, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         user = self.create_user(email, username, password, **extra_fields)
#         user.role = 'admin'
#         user.save()
#         return user
