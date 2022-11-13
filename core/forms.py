from django import forms
from core.validators import gmail_validation

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Full name",
        max_length=50,
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
