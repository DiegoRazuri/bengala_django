from django.contrib import admin
from .models import Award, Certification

# Register your models here.
@admin.register(Award)
class AdminAwards(admin.ModelAdmin):
    list_display = ('enterprise', 'title', 'subtitle', 'image', 'externalUrl',)

@admin.register(Certification)
class AdminCertifications(admin.ModelAdmin):
    list_display = ('enterprise', 'image',)