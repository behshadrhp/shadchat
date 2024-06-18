from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


class LoginView(View):
    """
    This class is for login user.
    """

    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect("home")
        else:
            context = {}
            return render(request, "account/login.html", context)
        
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
