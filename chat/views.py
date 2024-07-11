from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.db.models import Q
from django.views import View

from chat.models import Message

User = get_user_model()


class PVChatView(View):
    """
    This class is for rendering chat on pv.
    """
    
    def get(self, request, username):
        person = User.objects.get(username=username)
        user = request.user
        
        messages = Message.objects.select_related("user").select_related("send_message_to").filter(
            Q(user=user, send_message_to=person) | 
            Q(user=person, send_message_to=user)
        ).order_by('created')
        
        context = {"person": person, "messages": messages}
        return render(request, "chat/pv.html", context)
