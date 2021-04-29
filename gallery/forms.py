from django import forms
from .models import Art
  
  
# creating a form
class ArtForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = Art
  
        # specify fields to be used
        fields = [
            'artid',
            "artist",
            "desc",
            'iscolor',
            'artcost',
            'artdate',
            'artimg',
        ]
        widgets = {
            'artist': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            #'iscolor': forms.BooleanField(attrs={'class':'form-control'}),
            #'artcost': forms.FloatField(attrs={'class':'form-control'})
            'artdate': forms.DateInput(),
            #'artimg' : forms.FileInput()
        }