from django.contrib import admin
from .models import SiteSettings, ContactLead


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "whatsapp_number", "contact_email", "updated_at")


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "source", "created_at")
    list_filter = ("source", "created_at")
    search_fields = ("full_name", "email", "phone")
