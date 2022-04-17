from django.shortcuts import render
from django.views.generic import View
from .models import Category, Donation, Institution

# Create your views here.


# Langing Page View
class LandingPage(View):
    template_name = 'main_app/index.html'

    def get(self, request):
        donation = sum(Donation.objects.all().values_list('quantity', flat=True))
        institution = len(Institution.objects.all())
        ctx = {
            'donation': donation,
            'institution': institution
        }
        return render(request, self.template_name, ctx)


# Add User donation
class AddDonation(View):
    template_name = 'main_app/form.html'

    def get(self, request):
        return render(request, self.template_name)


# Confirmation for User donation
class DonationConfirmation(View):  # dodatkowy widok nie przewidziany na ten moment
    template_name = 'main_app/form-confirmation.html'

    def get(self, request):
        return render(request, self.template_name)


# User Login View
class Login(View):
    template_name = 'main_app/login.html'

    def get(self, request):
        return render(request, self.template_name)


# User Registration View
class Register(View):
    template_name = 'main_app/register.html'

    def get(self, request):
        return render(request, self.template_name)