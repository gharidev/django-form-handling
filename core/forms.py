from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Full name",
        max_length=50,
    )
    email = forms.EmailField(
        max_length=100,
        required=False,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 7}
        )
    )
