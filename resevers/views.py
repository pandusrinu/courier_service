from django.shortcuts import redirect, render

from.forms import SignUpForm, CourierServiceForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CourierService
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.post)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request,"Unsuccessful registration. Invalid information:")
    form = SignUpForm()
    return render(request=request, template_name="courier_service/signup.html",context={"SignUpForm":form})

def login_request(request):
    if request.method ==  'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="courier_service/login.html",context={"login_request":form})
def logout_request(request):
    logout(request)
    messages.info(request, "You hava successfully logged out.")
    return redirect("login")

class CourierServiceListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = CourierService

class CourierServiceCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = CourierService
    success_url = reverse_lazy('index')
    fields = ('receiver_name', 'contact_number', 'area', 'pickup_address', 'delivery_address', 'package_dimension', 'weight', 'service')

class CourierServiceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = CourierService
    success_url = reverse_lazy('index')
    fields = ('receiver_name', 'contact_number', 'area', 'pickup_address', 'delivery_address', 'package_dimension', 'weight', 'service')

class CourierServiceDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = CourierService
    success_url = reverse_lazy('index')


