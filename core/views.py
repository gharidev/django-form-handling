from django.views.generic import View
from django.shortcuts import render

from core.forms import ContactForm

class ContactView(View):
    
    def get(self, request):
        form = ContactForm() # Unbound Instantiation
        return render(request, "core/contact.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST) # Bound Instantiation
        if form.is_valid():
            return render(request, "core/success.html", {"data": form.cleaned_data})
        else:
            return render(request, "core/contact.html", {"form": form})