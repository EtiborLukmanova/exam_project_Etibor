from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Sweets, CustomUserComment


class SweetModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'description', 'create_at']
    list_filter = ['create_at']


admin.site.register(Sweets, SweetModelAdmin)
admin.site.register(CustomUserComment)

