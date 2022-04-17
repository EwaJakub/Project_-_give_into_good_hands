from django.shortcuts import render
from django.views.generic import View
from random import sample

from .models import Category, Donation, Institution

# Create your views here.


"""
Langing Page View, counts all quantity of donations (bags sum) and all donated institutions.
Shows three insitutions added to base of application, splitted on base of institutions types on each view.
"""
class LandingPage(View):
    template_name = 'main_app/index.html'

    def get(self, request):
        donation = sum(Donation.objects.all().values_list('quantity', flat=True))
        # show all of supported institutions, not only added -->
        institution = len(set(Donation.objects.all().values_list('institution', flat=True)))
        # institution = len(Institution.objects.all()) --> show all added institutions
        foundations = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        ctx = {
            'donation': donation,
            'institution': institution,
            'foundations': foundations,
            'organizations': organizations,
            'local_collections': local_collections,
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