from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class DoctorSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "line",
            "city",
            "state",
            "pincode",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()

    def __init__(self, *args, **kwargs):
        super(DoctorSignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


class PatientSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "profile_picture",
            "email",
            "line",
            "city",
            "state",
            "pincode",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()

    def __init__(self, *args, **kwargs):
        super(PatientSignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
