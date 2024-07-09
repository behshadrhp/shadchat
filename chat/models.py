from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    """
    This class is for create Message.
    """
    
    # primary key field and user relationship 
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_message")
    send_message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_send_message_to")
    
    # initial information
    message = models.TextField()
    has_seen_been = models.BooleanField(default=False)
    
    # create Time
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        indexes = [
            models.Index(fields=["user",]),
        ]
