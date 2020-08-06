from django.contrib import admin
from .models import *

# Register your models here.


def approve_application(modeladmin, request, queryset):
    for query in queryset:
        query.approve(request)


approve_application.short_description = "Approve and allocate resources"


class ApplicationAdmin(admin.ModelAdmin):
    actions = [approve_application,]
    list_display = ['name', 'email', 'employment_type', 'application_purpose', 'institution']


admin.site.register(Application, ApplicationAdmin)