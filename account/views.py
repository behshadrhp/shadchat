from django.contrib.auth import logout, authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from account.models import Profile
from account.forms import ProfileForm 
from utils.account.choices import GenderType

User = get_user_model()


class LoginView(View):
    """
    This class is for login user.
    """

    def get(self, request):
        
        if not request.user.is_authenticated:
            context = {}
            return render(request, "account/login.html", context)
        return redirect("dashboard")
        
    def post(self, request):
        
        if not request.user.is_authenticated:            
            username = request.POST.get("username").lower()
            password = request.POST.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login is successful")
                return redirect("dashboard")
            else:
                messages.error(request, "Your username or password is invalid")
                return redirect("login")
        return redirect("dashboard")


class RegisterView(View):
    """
    This class is for creating a User Account.
    """
    
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "account/register.html")
        else:
            return redirect("dashboard")
        
    def post(self, request):
        if not request.user.is_authenticated:
            username = request.POST.get("username").lower()
            email = request.POST.get("email").lower()
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            if password1 != password2:
                messages.error(request, "Your passwords do not match")
                return redirect("register")
            
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                )
                user.save()
            except Exception as e:
                messages.error(request, "The username or password entered is not valid, choose a valid username and strong password")
                return redirect("register")
            
            authenticated_user = authenticate(request, username=username, password=password1)
                
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, "Registration successful")
                return redirect("dashboard")
            else:
                messages.error(request, "Authentication failed. Please try logging in.")
                return redirect("login")
        else:
            return redirect("dashboard")


class LogoutView(View):
    """
    This class is for Logout user.
    """

    def get(self, request):
        logout(request)
        return redirect("home")
    
    def post(self, request):
        logout(request)
        return redirect("home")


class DashboardView(View):
    """
    This class is for rendering dashboard page.
    """
    
    def get(self, request):
        if request.user.is_authenticated:
            users = Profile.objects.select_related("user").all()
            
            context = {"users": users}
            return render(request, "account/dashboard.html", context)
        else:
            return redirect("login")


class ProfileView(View):
    """
    This class is for rendering Profile page.
    """
    
    def get(self, request):
        if request.user.is_authenticated:
            user_profile = Profile.objects.select_related("user").get(user=request.user)
            form = ProfileForm(instance=user_profile)
            
            gender_choices = GenderType.choices
            context = {"user": request.user, "form": form, "gender_choices": gender_choices}
            return render(request, "account/profile.html", context)
        else:
            return redirect("login")
    
    def post(self, request):
        if request.user.is_authenticated:
            user_profile = Profile.objects.select_related("user").get(user=request.user)
            form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile Updated")
                return redirect("dashboard")
            
            gender_choices = GenderType.choices
            context = {"user": request.user, "form": form, "gender_choices": gender_choices}
            return render(request, "account/profile.html", context)
        else:
            return redirect("login")
