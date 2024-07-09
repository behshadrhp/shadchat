from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View

User = get_user_model()


class PVChatView(View):
    """
    This class is for rendering chat on pv.
    """
    
    def get(self, request, username):
        person = User.objects.get(username=username)
        
        context = {"person": person}
        return render(request, "chat/pv.html", context)
