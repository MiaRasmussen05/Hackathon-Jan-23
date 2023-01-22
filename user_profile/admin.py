from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'age',
        'savings',
        'salary_pre',
        'salary_post',
        'expences',
    )

    ordering = (
        'user',
    )


admin.site.register(UserProfile, UserProfileAdmin)