from django.contrib import admin

# Register your models here.
from .models import Enterpriseprofile, Client

@admin.register(Enterpriseprofile)
class AdminEnterpriseprofile(admin.ModelAdmin):
    list_display = ('companyName', 'legalId', 'industry',)
    list_filter = ('industry',)

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('enterprise', 'client', 'status')
