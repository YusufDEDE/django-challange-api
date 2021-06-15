from django.db.models import signals
from django.dispatch import receiver
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


@receiver(signals.post_save, sender=Profile)
def create_profile_user(sender, instance, created, **kwargs):
    """listen profile models after auth user create/update"""
    if created:
        try:
            _user = User.objects.get(username=instance.username)
        except ObjectDoesNotExist:
            _user = User(
                first_name=instance.first_name,
                last_name=instance.last_name,
                username=instance.username,
                email=instance.email,
                is_staff=instance.status,
            )
            _user.set_password(instance.password)
            _user.save()

        instance.user = _user
        instance.save()

    instance.user.first_name = instance.first_name
    instance.user.last_name = instance.last_name
    instance.user.username = instance.username
    instance.user.password = make_password(instance.password)
    instance.user.email = instance.email
    instance.user.is_staff = instance.status
    instance.user.save()


@receiver(signals.post_delete, sender=Profile)
def delete_profile_user(sender, instance, **kwargs):
    """listen profile models after auth user delete"""
    if instance.user:
        instance.user.delete()
