from django import forms
from django.core.exceptions import ValidationError
from core.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ["name", "content"]
        # exclude = ["name"]

    def clean(self):
        """
        Raise `ValidationError` if user didn't provide both name and email.
        """
        cleaned_data = super().clean() # Making sure default cleaning is being done.
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")

        if not name and not email:
            raise ValidationError("Please provide name or email.")
        
        return cleaned_data

