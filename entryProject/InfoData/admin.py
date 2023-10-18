from django.contrib import admin

# Register your models here.
from InfoData.models import InfoModal

class InfoModalAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email_address", "mobile_number", "description", "response_status"]


admin.site.register(InfoModal, InfoModalAdmin)