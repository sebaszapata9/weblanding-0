from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default="Kumateq")
    slogan = models.CharField(max_length=180, blank=True)
    whatsapp_number = models.CharField(
        max_length=20,
        help_text="Ej: +51987654321 (incluye código de país)"
    )
    contact_email = models.EmailField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración del sitio"
        verbose_name_plural = "Configuración del sitio"

    def __str__(self):
        return self.site_name


class ContactLead(models.Model):
    SOURCE_CHOICES = [
        ("web", "Web"),
        ("whatsapp", "WhatsApp"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("other", "Otro"),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField(blank=True)

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="web")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.created_at:%Y-%m-%d})"
