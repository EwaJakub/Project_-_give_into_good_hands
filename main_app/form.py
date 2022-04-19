from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# form for user Registration
class AddUserForm(UserCreationForm):

    # Class Meta for creating a form
    class Meta:
        model = User  # form based on User model in django auth
        fields = (
            'username', "first_name", "last_name", "email", "password1", "password2"
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