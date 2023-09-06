from django.contrib import admin

from .models import TerroristGroup
# Register your models here.
@admin.register(TerroristGroup)
class TerroristGroupAdmin(admin.ModelAdmin):
    pass
