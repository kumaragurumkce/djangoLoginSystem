# accounts/urls.py
from django.urls import path
from .views import (
    company_admin_signup,
    client_customer_signup,
    CustomLoginView,
    CustomLogoutView,
    home,
    company_list,
    product_list,
    LoginView
)

urlpatterns = [
    path('signup/company-admin/', company_admin_signup, name='company_admin_signup'),
    path('signup/client-customer/', client_customer_signup, name='client_customer_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', home, name='home'),  # The homepage accessible to all logged-in users
    path('company-list/', company_list, name='company_list'),  # Accessible only by company-admin
    path('product-list/', product_list, name='product_list'),  # Accessible only by client-customer
]
