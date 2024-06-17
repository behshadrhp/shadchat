from django.shortcuts import render
from django.views import View


class HomeView(View):
    """
    Rendering Home page.
    """
    
    def get(self, request):
        
        context = {}
        return render(request, "home/index.html", context)
