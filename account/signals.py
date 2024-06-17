from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from account.models import Profile, Settings


User = get_user_model()

@receiver(post_save, sender=User)
def set_new_user_inactive(sender, instance, created, **kwargs):
    """
    Deactivation of the normal user account until it is accepted by the admin.
    """

    if created:  # Checking the status of the created user instance
        if instance.is_superuser == False:
            instance.save()


# create user profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create profile for new account.
    """

    if created:
        Profile.objects.create(user=instance)


# create user account settings
@receiver(post_save, sender=User)
def create_settings(sender, instance, created, **kwargs):
    """
    Create user settings for new account.
    """

    if created:
        Settings.objects.create(user=instance)
