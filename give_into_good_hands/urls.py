"""give_into_good_hands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app import views as main_views

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-page'),  # {% url 'admin-page' %} nie działa
    path('', main_views.LandingPage.as_view(), name='landing-page'),
    path('accounts/login/', main_views.Login.as_view(), name='login'),  # samo login nie działało
    path('register/', main_views.Register.as_view(), name='register'),
    path('add-donation/', main_views.AddDonation.as_view(), name='add-donation'),
    path('donation-confirmation/', main_views.DonationConfirmation.as_view(), name='donation-confirmation'),
    path('logout/', main_views.log_out, name='logout'),
    path('my-profile/', main_views.UserProfileView.as_view(), name='my-profile'),
]
