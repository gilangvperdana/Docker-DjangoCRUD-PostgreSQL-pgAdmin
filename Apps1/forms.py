from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','NIM','Mobile','position')
        labels = {
            'fullname':'Name',
            'NIM':'Student ID',
            'Mobile':'Class',
            'position':'Gender '
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['NIM'].required = False