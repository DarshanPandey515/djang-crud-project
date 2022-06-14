from django import forms
from .models import Student
from django.core import validators

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('Student_Name','Student_Class','Student_Age','Student_Section','Student_Sex')
        widgets = {
            'Student_Name': forms.TextInput(attrs={'class':'form-control focus:shadow-outline'}) ,
            'Student_Class': forms.Select(attrs={'class':'form-control'}) ,
            'Student_Age': forms.NumberInput(attrs={'class':'form-control'}) ,
            'Student_Section': forms.Select(attrs={'class':'form-control'}) ,
            'Student_Sex': forms.Select(attrs={'class':'form-control'}) ,
        }  