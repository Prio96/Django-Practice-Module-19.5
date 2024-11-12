from django import forms
from models import Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        exclude=['release_date']
        labels={
            'title':'Album title'
        }
        