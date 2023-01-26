from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    home,
    doctors,
    patients,
    DoctorSignUpView,
    PatientSignUpView,
    SignUpView,
    DoctorDashBoard,
    PatientDashBoard,
)

urlpatterns = [
    path("", home, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name="doctor/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/doctor/", DoctorSignUpView.as_view(), name="signup_doctor"),
    path("signup/patient/", PatientSignUpView.as_view(), name="signup_patient"),
    path('doctors',views.doctors, name='doctors'),
    path('patients/',views.patients, name='patients'),
    path("doctordashboard/", DoctorDashBoard.as_view(), name="doctor"),
    path("patient/", PatientDashBoard.as_view(), name="patient"),
]
