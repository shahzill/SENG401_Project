from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from stuhub.models import Comment

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('courseName', 'professorRating', 'professorN', 'courseComment', 'commenterName')
        