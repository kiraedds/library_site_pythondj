from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    birthYear = forms.IntegerField(label='Year of birth', max_value=2050)
    facePhoto = forms.CharField(label='URL to authors\' photo')

    class Meta:
        ordering = ['surname']
