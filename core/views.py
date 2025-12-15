from django.shortcuts import render, redirect
from .models import SiteSettings
from .forms import ContactLeadForm

#creamos las vistas aquí
def home(request):

    site  = SiteSettings.objects.order_by("-updated_at").first()

    if request.method == "POST":
        form = ContactLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.source = "web"
            lead.save()
            return redirect("core:thanks")
    else:
        form = ContactLeadForm()



    return render(request, "core/home.html", {"site": site , "form": form})


def thanks(request):
    return render(request, "core/thanks.html")