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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.LandingPage.as_view(), name='landing-page'),
    path('login/', main_views.Login.as_view(), name='login'),
    path('register/', main_views.Register.as_view(), name='register'),
    path('add-donation/', main_views.AddDonation.as_view(), name='add-donation'),
    path('donation-confirmation/', main_views.DonationConfirmation.as_view(), name='donation-confirmation'),
]
