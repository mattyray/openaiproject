from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# accounts/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('/')  # Redirect to the home page



class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"