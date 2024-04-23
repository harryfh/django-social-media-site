from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    title = forms.CharField(required=True,         widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "TITLE...",
                "class": "rounded btn text-lg bg-yellow text-red w-full mb-3 jersey",
            }
        ),
        label="",)
    content = forms.CharField(required=True,         widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "BLOG...",
                "class": "w-full rounded btn text-lg bg-yellow text-red jersey",
            }
        ),
        label="",)
    class Meta:
        model = BlogPost
        exclude = ("user",  )