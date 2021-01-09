from django import forms
from .models import Comment
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25,
         widget=forms.TextInput(attrs={
             'class':'form-control',
             'id':'nameInput'}))
    email=forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "id": "InputEmail",
                   "aria-describedby": "emailHelp"
                   }))
    to=forms.EmailField(widget=forms.TextInput(
            attrs={"class": "form-control",
                    'id':'emailTo'}))
    comments=forms.CharField(required=False,
                 widget=forms.Textarea(
                     attrs={"class": "form-control",
                            'id':'comments',
                            'rows':'3'}))

class CommentForm(forms.Form):
    name=forms.CharField(max_length=25,
             widget=forms.TextInput(attrs={
                 'class':'form-control',
                 'id':'nameInput'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={
                 'class':'form-control',
                 'id':'emailInput',
                 'aria-describedby':'EmailHelp'}))
    body=forms.CharField(required=False,
                         widget=forms.Textarea(attrs={
                             'class':'form-control',
                             'id':'comment',
                             'rows':'3'}))




