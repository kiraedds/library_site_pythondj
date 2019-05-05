from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)

    class Meta:
        ordering = ['surname']
