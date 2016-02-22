from django.contrib import admin

# Register your models here.
from .models import Catalog

@admin.register(Catalog)
class AdminCatalog(admin.ModelAdmin):
    list_display = ('enterprise', 'image', 'title', 'subtitle', 'description',)
    list_filter = ('enterprise',)