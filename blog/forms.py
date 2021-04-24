from django import forms
from .models import Comment, Post, User,PostPoint
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




class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'inputLogin',
                'class':'form-control',
                'placeholder':'Логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'id':'inputPassword',
                'class':'form-control',
                'placeholder':'Пароль'}))

class PostAddForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','short_description',
                'image','tags')

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name',
                'username','email')

class UserCreateForm(forms.ModelForm):
    password=forms.CharField(max_length=40,widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('first_name','last_name',
                'username','email','password')



class PostPointForm(forms.ModelForm):
    class Meta:
        model=PostPoint
        fields=('post_point_header','post_point_text','post_image')


class SearchForm(forms.Form):
    query=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mr-sm-2',
        'type':'search',
        'placeholder':'Search',
        'aria-label':'Search'
    }))
