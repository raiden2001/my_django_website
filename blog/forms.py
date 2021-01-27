from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:  # give what kind of form
        model = Post
        # which fields want u to create
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # inhertane from Function model comment
        # timezone.now() makes time exactly automactically
        # comma hodl more value
        fields = ('text',)
