from django import forms
from .models import Comment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {
            'name' : forms.TextInput(attrs={'placeholder':'name'}),
            'email' : forms.TextInput(attrs={}),
            'content' : forms.TextInput(attrs={})
        }
