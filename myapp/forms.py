from django import forms
from myapp.models import School
#from django.core import validators

# def check_for_m(value):
#     if value[0].upper() != 'm':
#         raise forms.ValidationError('Should start with M/m')
# class Login(forms.Form):
#     name = forms.CharField(validators = [check_for_m])
#     name = forms.CharField()
#     vname = forms.CharField()
#     email = forms.EmailField()
#     comments = forms.CharField(widget = forms.Textarea)
#     password = forms.CharField(widget = forms.PasswordInput)
#
#     def clean(self):
#         val = super().clean()
#         name = val['name']
#         vname = val['vname']
#
#         if name != vname:
#             raise forms.ValidationError('Name should be same')

class UserForms(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
