from django.contrib import admin
from .models import CalcFunding

class CalcFundingAdmin(admin.ModelAdmin):
    list_display = (
        'cost',
        'savings',
        'salary_pre',
        'salary_post',
        'expences',
    )

    ordering = (
        'cost',
    )


admin.site.register(CalcFunding, CalcFundingAdmin)
