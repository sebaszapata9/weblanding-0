from django import forms
from .models import ContactLead

class ContactLeadForm(forms.ModelForm):
    class Meta:
        model = ContactLead
        fields = ["full_name", "email", "phone", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }
