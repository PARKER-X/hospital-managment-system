from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView
from .models import CustomUser
from .forms import DoctorSignUpForm, PatientSignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect("/doctor")
        elif request.user.is_patient:
            return redirect("/patient")
        else:
            return render(request, "doctor/index.html", {})

    else:
        return render(request, "doctor/index.html", {})


def doctors(request):
    return render(request, 'doctor/base.html',{})



class DoctorDashBoard(UserPassesTestMixin, TemplateView):
    template_name = "doctor/dashboard.html"

    def test_func(self):
        return self.request.user.is_doctor


class PatientDashBoard(UserPassesTestMixin, TemplateView):
    template_name = "home.html"

    def test_func(self):
        return self.request.user.is_patient


class SignUpView(TemplateView):
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class DoctorSignUpView(CreateView):
    model = CustomUser
    form_class = DoctorSignUpForm
    template_name = "doctor/register.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        return redirect("/")


class PatientSignUpView(CreateView):
    model = CustomUser
    form_class = PatientSignUpForm
    template_name = "doctor/register.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        return redirect("/")



def home(request):
    return render(request, 'doctor/index.html')

def doctor(request):
    return render(request, 'doctor/base.html')

def patients(request):
    return render(request, 'doctor/newbase.html')

def dashboard(request):
    return render(request, 'doctor/dashboard.html')