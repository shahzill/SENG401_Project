from django import forms
from django.forms import ModelForm

from stuhub.models import Applicant

class applyTutorForm(ModelForm):

    class Meta:
        model = Applicant
        fields = ['appUCID', 'appFullName', 'appEmail', 'appPhoneNum', 'course', 'major','year']
        