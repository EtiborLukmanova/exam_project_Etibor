from django import forms
from .models import Sweets, CustomUserComment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SweetForm(forms.ModelForm):
    class Meta:
        model = CustomUserComment
        fields = ['comment']


class UpdateSweetForm(forms.ModelForm):
    class Meta:
        model = Sweets
        fields = ['name', 'description', 'company', 'image_sweet']

    def __init__(self, *args, **kwargs):
        super(UpdateSweetForm, self).__init__(*args, **kwargs)


class CreateSweetForm(forms.ModelForm):
    class Meta:
        model = Sweets
        fields = ['name', 'description', 'company', 'image_sweet', 'price']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CustomUserComment
        fields = (
           'comment',
           'star_given',
        )


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserComment
        fields = (
           'comment',
           'star_given',
        )