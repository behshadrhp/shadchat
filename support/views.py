from django.shortcuts import render
from django.views import View


class ContactUSView(View):
    """
    Rendering ContactUS page.
    """
    
    def get(self, request):
        
        context = {}
        return render(request, "home/contact_us.html", context)
