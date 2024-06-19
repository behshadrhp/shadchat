from django.shortcuts import render
from django.views import View


class HomeView(View):
    """
    Rendering Home page.
    """
    
    def get(self, request):
        
        context = {}
        return render(request, "home/index.html", context)


class AboutUSView(View):
    """
    Rendering AboutUS page.
    """
    
    def get(self, request):
        
        context = {}
        return render(request, "home/about_us.html", context)


class ContactUSView(View):
    """
    Rendering ContactUS page.
    """
    
    def get(self, request):
        
        context = {}
        return render(request, "home/contact_us.html", context)
