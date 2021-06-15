from django.contrib import admin
from .models import Profile
from csvexport.actions import csvexport


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    exclude = ('user', )
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'about_us')
    search_fields = ('username', 'first_name', 'last_name', 'about_us')
    actions = [csvexport]
