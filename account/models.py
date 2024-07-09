from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models, transaction

from utils.account.choices import GenderType
from utils.validator import fields
from utils.path import path


class User(AbstractUser):
    """
    This class is for create User Model.
    """
    
    # primary key
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False, db_index=True)
    
    # information user authentication
    username = models.CharField(max_length=15, unique=True, validators=[fields.username_regex])
    email = models.EmailField(unique=True, validators=[fields.email_regex, fields.validate_email])
    
    # enable account
    is_enable = models.BooleanField(default=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    class Meta:
        ordering = ["-date_joined", "is_superuser", "is_staff", "is_active"]
        verbose_name = "User"
        verbose_name_plural = "Users"
        
        indexes = [
            models.Index(fields=["username",]),
        ]
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # username and email convert to lower case
        self.username = self.username.lower()
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class Profile(models.Model):
    """
    This class is for completing the user profile.
    """

    # primary key field and user profile relationship 
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    
    # initial information
    avatar = models.ImageField(
        default="default/avatar.png", 
        upload_to=path.user_profile_avatar_upload_path, 
        validators=[fields.validate_file_size_volume, fields.validate_image_file_extension]
    )
    first_name = models.CharField(max_length=15, null=True, blank=True, validators=[fields.name_regex])
    last_name = models.CharField(max_length=15, null=True, blank=True, validators=[fields.name_regex])
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GenderType.choices, default=GenderType.OTHER)  # choice gender
    bio = models.TextField(max_length=50, null=True, blank=True)

    # create - update Time
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated"]
        verbose_name = "User Profile"
        verbose_name_plural = "Profiles"
        indexes = [
            models.Index(fields=["user",]),
        ]

    def __str__(self):
        return str(self.user.username)
    
    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.id:
                existing = Profile.objects.filter(id=self.id).first()
                if existing:
                    if existing.avatar != self.avatar and "default/" not in existing.avatar.path:
                        existing.avatar.delete(save=False)
        
        super().save(*args, **kwargs)


class Settings(models.Model):
    """
    This class is for apply permission on user account.
    """

    # primary key field and user account relationship 
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_settings")

    # user access
    admin = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    writer = models.BooleanField(default=False)

    # send message
    notification = models.BooleanField(default=False)

    # account disable
    disable = models.BooleanField(default=False)

    # create - update Time
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated"]
        verbose_name = "Account Settings"
        verbose_name_plural = "Settings"
        indexes = [
            models.Index(fields=["user",]),
        ]

    def __str__(self):
        return str(self.user.username)


class UserActivity(models.Model):
    """
    This class is for Monitoring and Watching user activity.
    last activity + total time activity.
    """
    
    # field information user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_activity")
    last_activity = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["last_activity"]
        verbose_name = "User Activate"
        verbose_name_plural = "Users Activity"
        indexes = [
            models.Index(fields=["user",]),
        ]

    def __str__(self):
        return str(self.user.username)
