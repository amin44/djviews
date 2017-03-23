from django import forms
from .models import PostModel

class PostModelform(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['title','content']