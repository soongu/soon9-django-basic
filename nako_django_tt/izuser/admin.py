from django.contrib import admin
from .models import IzUser


class IzUserAdmin(admin.ModelAdmin):
    list_display = 'username', 'password'


admin.site.register(IzUser, IzUserAdmin)
