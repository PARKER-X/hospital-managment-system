from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator


class CustomAccountManager(BaseUserManager):
    def create_user(
        self, email, username, first_name, last_name, password, **other_fields
    ):
        if not username:
            raise ValueError("username required!")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email, username, first_name, last_name, password, **other_fields
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned superuser=True")

        return self.create_user(
            email, username, first_name, last_name, password, **other_fields
        )


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField("Doctor", default=False)
    is_patient = models.BooleanField("Patient", default=False)
    profile_picture = models.ImageField(upload_to="media/")
    line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField(
        validators=[
            RegexValidator(
                regex="^[1-9][0-9]{5}$",
                message="Pincode must be of six digits",
                code="invalid pincode",
            )
        ]
    )
    objects = CustomAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
        "line",
        "city",
        "state",
        "pincode",
    ]

    def __str__(self):
        return self.username
