from django.contrib import admin
from django.contrib.auth.models import User

from myweb_main.models import Post, Profile
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin

admin.site.register(Post)


class ProfileInline(admin.StackedInline):
    model = Profile

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(UserBaseAdmin):
    inlines = (
        ProfileInline,
    )