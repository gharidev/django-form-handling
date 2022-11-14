from django.views.generic import View
from django.shortcuts import render

from core.forms import ContactForm
from core.utils import handle_uploaded_file

class ContactView(View):
    
    def get(self, request):
        form = ContactForm() # Unbound Instantiation
        return render(request, "core/contact.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST, request.FILES) # Bound Instantiation
        if form.is_valid():
            if form.cleaned_data["attachment"]:
                handle_uploaded_file(form.cleaned_data["attachment"])
            return render(request, "core/success.html", {"data": form.cleaned_data})
        else:
            return render(request, "core/contact.html", {"form": form})