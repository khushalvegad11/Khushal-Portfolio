from django.contrib import admin
from contactenquiry.models import contactEnquiry

class contactEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(contactEnquiry,contactEnquiryAdmin)


# Register your models here.
