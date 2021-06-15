from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Last Name")
    username = models.CharField(max_length=99, verbose_name="Username")
    password = models.CharField(max_length=99, verbose_name="Password")
    email = models.EmailField(max_length=250, verbose_name="Email")
    phone = models.CharField(max_length=14, null=True, blank=True, verbose_name="Phone")
    about_us = models.CharField(max_length=1000, null=True, blank=True, verbose_name="About Us")
    status = models.BooleanField(default=False, verbose_name="status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
