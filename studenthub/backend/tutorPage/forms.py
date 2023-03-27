from django import forms
from django.forms import ModelForm

from stuhub.models import Applicant

class applyTutorForm(ModelForm):

    class Meta:
        model = Applicant
        fields = ['appFName', 'appLName', 'appUCID', 'course', 'major', 'year', 'ques1','ques2']
        