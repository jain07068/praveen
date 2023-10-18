from django.contrib import admin
from  django.contrib.auth.models  import  Group, User

# Register your models here.
from InfoData.models import InfoModal
from import_export.admin import ExportActionMixin

class InfoModalAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["first_name", "email_address", "mobile_number", "description", "response_status"]


admin.site.register(InfoModal, InfoModalAdmin)

admin.site.site_header  =  "Info Admin"
admin.site.site_title  =  "Info Admin"
admin.site.index_title  =  "Event"

admin.site.unregister(Group)
admin.site.unregister(User)