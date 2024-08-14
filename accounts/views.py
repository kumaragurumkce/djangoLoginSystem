# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CompanyAdminSignUpForm, ClientCustomerSignUpForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
def company_admin_signup(request):
    if request.method == 'POST':
        form = CompanyAdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CompanyAdminSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def client_customer_signup(request):
    if request.method == 'POST':
        form = ClientCustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = ClientCustomerSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



# accounts/views.py

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    # Redirect to the login page after logout
    next_page = reverse_lazy('login')



@login_required
def home(request):
    return render(request, 'accounts/home.html')

@login_required
def company_list(request):
    if request.user.is_company_admin:
        return render(request, 'accounts/company_list.html')
    else:
        return redirect('home')

@login_required
def product_list(request):
    if request.user.is_client_customer:
        return render(request, 'accounts/product_list.html')
    else:
        return redirect('home')