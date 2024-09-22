from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile


@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwags):
    if created:
        profile.objects.create(user=instance)

def save_profile(sender,instance,**kwags):
    instance.profile.save()