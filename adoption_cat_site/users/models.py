# # from django.db import models
# # from django.core.validators import RegexValidator
# # from django.contrib.auth.models import AbstractUser, BaseUserManager
# #
# #
# # class UserManager(BaseUserManager):
# #     def create_user(self, email, password=None):
# #         if not email:
# #             raise ValueError('Users must have an e-mail address.')
# #
# #         user = self.model(
# #             email=self.normalize_email(email)
# #         )
# #         user.set_password(password)
# #         user.save(using=self._db)
# #
# #         return user
# #
# #     def create_superuser(self, email, password=None):
# #         user = self.create_user(email, password)
# #         user.is_superuser = True
# #         user.is_staff = True
# #         user.save(using=self._db)
# #
# #         return user
# #
# #
# # class UserAccount(AbstractUser):
# #     # username = None
# #     address = models.CharField(max_length=200)
# #     email = models.EmailField(verbose_name='email', max_length=255, unique=True)
# #     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
# #                                  message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
# #     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
# #
# #     objects = UserManager()
# #
# #     def __str__(self):
# #         return self.email
# #
# #     def __repr__(self):
# #         return self.__str__()
#
# from django.db import models
# from django.templatetags.static import static
# from django.conf import settings
# from django.contrib.auth.models import AbstractUser, BaseUserManager
#
#
# class AuthUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an e-mail address.')
#
#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, password=None):
#         user = self.create_user(email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#         return user
#
#
# class AuthUser(AbstractUser):
#     username = None
#     email = models.EmailField(verbose_name='email', max_length=255, unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = AuthUserManager()
#
#     def __str__(self):
#         return self.email
#
#     def __repr__(self):
#         return self.__str__()
