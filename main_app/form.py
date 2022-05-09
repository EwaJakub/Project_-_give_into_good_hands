from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

# form for user Registration
class AddUserForm(UserCreationForm):

    # Class Meta for creating a form
    class Meta:
        model = User  # form based on User model in django auth
        fields = (
            "username", "first_name", "last_name", "email", "password1", "password2"
        )

    def __init__(self, *args, **kwargs):  # inheritance
        super().__init__(*args, **kwargs)

        for field_name in ("username", "password1", "password2"):
            self.fields[field_name].help_text = None    # hides default hints from User model to fill each field

    def clean(self):
        # calling super().clean() to get cleaned data on basis of django validators and adding our own validators
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        user = User.objects.filter(email=email).first()
        if user:
            self.add_error("email", "Użytkowik o podanym mailu już istnieje.")

        if password1 != password2:
            self.add_error("password2", "Hasła w obu polach muszą być jednakowe.")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    def clean(self):
        self.cleaned_data = super().clean()

        user = self.authenticate_via_email()
        if not user:
            return None
        else:
            self.user = user
        return self.cleaned_data

    def authenticate_user(self):
        return authenticate(
            username=self.user.username,
            password=self.cleaned_data['password'])

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)  # iexact niewrazliwe na wielkość liter
                if user.check_password(self.cleaned_data['password']):
                    return user
                else:
                    self.add_error("password", "Hasło niewłaściwe")
            except ObjectDoesNotExist:
                self.add_error("email", "Użytkowik o podanym mailu nie istnieje.")
        else:
            return None


class EditUserProfileForm(forms.Form):
    first_name = forms.CharField(label='Imię:', max_length=200, required=False)
    last_name = forms.CharField(label='Nazwisko:', max_length=200, required=False)
    email = forms.CharField(label='email', max_length=200)
    password = forms.CharField(label='Podaj hasło żeby potwierdzić zmiany', max_length=255, widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label='Hasło', max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', max_length=255, widget=forms.PasswordInput)