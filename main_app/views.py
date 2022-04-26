from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.core.exceptions import ObjectDoesNotExist

from .form import AddUserForm, LoginForm
from .models import Category, Donation, Institution

# Create your views here.



"""
Langing Page View, counts all quantity of donations (bags sum) and all donated institutions.
Shows insitutions added to database of application, splitted on the base of institutions types on each view.
"""
class LandingPage(View):
    template_name = 'main_app/index.html'

    # function for pagination
    def paginator(self, request, element):
        p = Paginator(element, 1)
        page_number = request.GET.get('page')
        page = p.get_page(page_number)
        return page

    def categories_list(self, element):
        categories = ', '.join(element.categories.all().values_list('name', flat=True))
        return categories

    def get(self, request):
        donation = sum(Donation.objects.all().values_list('quantity', flat=True))
        # show all of supported institutions, not only added -->
        institution = len(set(Donation.objects.all().values_list('institution', flat=True)))
        # institution = len(Institution.objects.all()) --> show all added institutions
        """ 
        in html file is a way of extracting all needed data only on basis of foundations, 
        organizations, local_collections 
        """
        foundations = Institution.objects.filter(type=1)
        for foundation in foundations:
            found_categories = self.categories_list(foundation)
        organizations = Institution.objects.filter(type=2)
        for organization in organizations:
            org_categories = self.categories_list(organization)
        local_collections = Institution.objects.filter(type=3)
        for local_collection in local_collections:
            loc_categories = self.categories_list(local_collection)
        # Pagination for each side
        page_1 = self.paginator(request, foundations)
        page_2 = self.paginator(request, organizations)
        page_3 = self.paginator(request, local_collections)
        # PAGINACJA NIE PRZESKAKUJE DO INNEJ STRONY!!
        ctx = {
            'donation': donation,
            'institution': institution,
            'foundations': foundations,
            'found_categories': found_categories,
            'organizations': organizations,
            'org_categories': org_categories,
            'local_collections': local_collections,
            'loc_categories': loc_categories,
            'page_1': page_1,
            'page_2': page_2,
            'page_3': page_3,
        }
        return render(request, self.template_name, ctx)



# Add User donation
class AddDonation(LoginRequiredMixin, View):
    template_name = 'main_app/form.html'
    permission_required = 'main_app.add_donation'

    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user:   # checking if user is in base
                ctx = {
                    'categories': Category.objects.all()
                }
                return render(request, self.template_name, ctx)
        except user.DoesNotExist:  # if user DoesNotExist
            messages.error(request, "Żeby cokolwiek oddać musisz być zalogowany!") # nie wyświetla się message error ?
            return redirect("login")
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
        return render(request, self.template_name, {"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = form.authenticate_user()  # authentication
            if user:  # user.is_authenticated
                login(request, user)  # login
                return redirect('/')
        elif form.has_error("email"):  # przekierowuje gdy powstaje form email error
            messages.error(request, "Tego adresu email nie ma w bazie. Załóż konto.")
            return redirect("register")

        return render(request, self.template_name, {"form": form})


# Log out funtion for logged users
@login_required  # requirement for user, that he needs to be logged in
def log_out(request):
    logout(request)
    return redirect("/")


# User Registration View
class Register(View):
    template_name = 'main_app/register.html'

    def get(self, request):
        return render(request, self.template_name, {"form": AddUserForm()})

    def post(self, request):
        form = AddUserForm(request.POST)
        logged_user = request.user.username
        if logged_user:
            messages.error(request, "Posiadasz już konto!")
            return render(request, self.template_name, {"form": form})
        elif form.is_valid():
            form.save()
            messages.success(request, "Użytkownik zarejestrowany pomyślnie! Zaloguj się, żeby korzystać z serwisu.")
            return redirect("login")
        else:
            messages.error(request, "Problem z rejestracją użytkownika. Spróbuj ponownie")
            return render(request, self.template_name, {"form": form})

