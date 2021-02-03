from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)


class PostForm(forms.ModelForm):
    class Meta:  # give what kind of form
        model = Post
        # which fields want u to create
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # inheritance from Function model comment
        # timezone.now() makes time exactly automactically
        # comma hodl more value 
        fields = ('text',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())  # imports password forms outline
    helper = FormHelper()  # if you want some help documentation
    helper.form_method = 'POST' # its post  for method is posted
    helper.add_input(Submit('Sign up', 'Sign up', css_class='btn-primary'))

    class Meta:
        model = User  # Django imports the user
        fields = ('username', 'email', 'password',) #output loing