from django.contrib import admin
from .models import Names


@admin.register(Names)
class NamesAdmin(admin.ModelAdmin):
    view_on_site = True
