# # from django import forms
# # from django.contrib.auth import get_user_model
# # from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
# # from .models import UserAccount
# #
# # UserAccount = get_user_model()
# #
# # class UserCreationForm(forms.Form):
# #     first_name = forms.CharField(max_length=255, required=True, label='First name')
# #     last_name = forms.CharField(max_length=255, required=True, label='Last name')
# #     username = forms.CharField(required=True, label='Username')
# #     email = forms.EmailField( max_length=255, required=True, label='Email')
# #     address = forms.CharField(required=True, label='Address')
# #     phone_number = forms.CharField(required=True, label='Phone Number')
# #
# #     password = forms.CharField(
# #         required=True,
# #         label='Password',
# #         widget=forms.PasswordInput,
# #         help_text=password_validators_help_text_html()
# #     )
# #     password_confirmation = forms.CharField(
# #         required=True,
# #         label='Confirm password',
# #         widget=forms.PasswordInput,
# #         help_text='Please confirm your password'
# #     )
# #
# #     def clean_username(self):
# #         username = self.cleaned_data.get('username')
# #
# #         try:
# #             UserAccount.objects.get(username=username)
# #         except UserAccount.DoesNotExist:
# #             return username
# #
# #         raise forms.ValidationError(f'{username} is already taken.')
# #
# #     def clean_password(self):
# #         first_name = self.cleaned_data.get('first_name')
# #         last_name = self.cleaned_data.get('last_name')
# #         username = self.cleaned_data.get('username')
# #         email = self.cleaned_data.get('email')
# #         address = self.cleaned_data.get('address')
# #         password = self.cleaned_data.get('password')
# #         phone_number = self.cleaned_data.get('phone_number')
# #
# #         user = UserAccount(
# #             first_name=first_name,
# #             last_name=last_name,
# #             username=username,
# #             email=email,
# #             address=address,
# #             phone_number=phone_number
# #         )
# #
# #         validate_password(password, user=user)
# #
# #         return password
# #
# #     def clean_password_confirmation(self):
# #         password = self.cleaned_data.get('password')
# #         password_confirmation = self.cleaned_data.get('password_confirmation')
# #
# #         if password_confirmation != password:
# #             raise forms.ValidationError('Password not confirmed.')
# #
# #         return password_confirmation
# #
# #     def save(self):
# #         first_name = self.cleaned_data.get('first_name')
# #         last_name = self.cleaned_data.get('last_name')
# #         username = self.cleaned_data.get('username')
# #         email = self.cleaned_data.get('email')
# #         address = self.cleaned_data.get('address')
# #         phone_number = self.cleaned_data.get('phone_number')
# #         password = self.cleaned_data.get('password')
# #
# #         user = UserAccount.objects.create_user(
# #             first_name=first_name,
# #             last_name=last_name,
# #             username=username,
# #             password=password,
# #             email=email,
# #             address=address,
# #             phone_number=phone_number
# #         )
# #
# #         return user
#
# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
#
# AuthUser = get_user_model()
#
#
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = AuthUser
#         fields = ['first_name', 'last_name', 'email']
#
#     password = forms.CharField(
#         max_length=255,
#         required=True,
#         label='Password',
#         widget=forms.PasswordInput,
#         help_text=password_validators_help_text_html()
#     )
#
#     password_confirmation = forms.CharField(
#         max_length=255,
#         required=True,
#         label='Confirm password',
#         widget=forms.PasswordInput,
#         help_text='Please confirm your password'
#     )
#
#     def clean_password(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         #username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         user = AuthUser(
#             first_name=first_name,
#             last_name=last_name,
#             #username=username
#         )
#
#         validate_password(password, user=user)
#
#         return password
#
#     def clean_password_confirmation(self):
#         password = self.cleaned_data.get('password')
#         password_confirmation = self.cleaned_data.get('password_confirmation')
#
#         if password_confirmation != password:
#             raise forms.ValidationError('Password not confirmed.')
#
#         return password_confirmation
#
#     def save(self, commit=True):
#         password = self.cleaned_data.get('password')
#         self.instance.set_password(password)
#
#         return super().save(commit)
#
#

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
