from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auths.users.models import User


@admin.register(User)
class ArvanUserAdmin(UserAdmin):
    pass