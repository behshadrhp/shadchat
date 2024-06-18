from django.contrib.auth import logout, authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

User = get_user_model()


class LoginView(View):
    """
    This class is for login user.
    """

    def get(self, request):
        
        if not request.user.is_authenticated:
            context = {}
            return render(request, "account/login.html", context)
        return redirect("home")
        
    def post(self, request):
        
        if not request.user.is_authenticated:            
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login is successful")
                return redirect("home")
            else:
                messages.error(request, "Your username or password is invalid")
                return redirect("login")
        return redirect("home")


class RegisterView(View):
    """
    This class is for create User Account.
    """
    
    def get(self, request):

        if not request.user.is_authenticated:
            context = {}
            return render(request, "account/register.html")
        else:
            return redirect("home")
        
    def post(self, request):
        
        if not request.user.is_authenticated:
            
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            if password1 != password2:
                messages.error(request, "Your password not match")
                return redirect("register")
            
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                )

            except:
                messages.error(request, "The username or password entered is not valid, choose a valid username and strong password")
                return redirect("register")
            
            authenticated_user = authenticate(request, username=username, password=password1)
                
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, "Login successful")
                return redirect("home")
            
        else:
            return redirect("home")


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
