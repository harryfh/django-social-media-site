from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):

    content = forms.CharField(required=True,         widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "blog...",
                "class": "rounded btn text-lg bg-yellow text-red jersey",
            }
        ),
        label="",)
    class Meta:
        model = BlogPost
        exclude = ("user", "title",  )