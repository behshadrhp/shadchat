from django.shortcuts import render
from django.views import View


class PVChatView(View):
    """
    This class is for rendering chat on pv.
    """
    
    def get(self, request):
        
        context = {}
        return render(request, "chat/pv.html", context)
