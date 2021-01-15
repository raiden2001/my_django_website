from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:  # give what kind of form
        model = Post
        # which fields want u to create
        fields = ( 'title', 'text')
