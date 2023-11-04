from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auths.users.models import User, UserProfile


class ArvanUserProfileInline(admin.StackedInline):
    model = UserProfile


@admin.register(User)
class ArvanUserAdmin(UserAdmin):
    inlines = (ArvanUserProfileInline,)
