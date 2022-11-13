from django import forms
from core.validators import gmail_validation
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Full name",
        max_length=50,
        required=False,
    )
    email = forms.EmailField(
        max_length=100,
        required=False,
        validators=[gmail_validation]
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 7}
        )
    )

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

