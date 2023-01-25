from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "username",
        "is_doctor",
        "is_patient",
    ]
    search_fields = ("email__startswith", "first_name__startswith")
    list_filter = ["is_doctor", "is_patient"]

    class Meta:
        ordering = "first_name"
