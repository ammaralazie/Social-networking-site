from django import forms
from .models import *

class Add_Post(forms.ModelForm):
    class Meta:
        model=Post
        fields=['content','image']
        widgets={'content':forms.Textarea(attrs={'rows':4,'placeholder':'add your post ...'})}

class Add_Commint(forms.ModelForm):
    class Meta:
        model=Commint
        fields=['body']
        widgets={'body':forms.TextInput(attrs={'placeholder':'add your commint ...'})}
