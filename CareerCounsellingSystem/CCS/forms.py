from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class ApprovalForm(forms.Form):
    Best_Course = forms.ChoiceField( choices=[('Male','Male'),('Female','Female')])
    Married = forms.ChoiceField( choices=[('Yes','Yes'),('No','No')])
    Education = forms.ChoiceField(choices=[('Graduated','Graduated'),('Not_Graduate','Not_Graduated')])
    Self_Employed = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Property_Area = forms.ChoiceField(choices=[('Rural','Rural'),('Semiurban','Semiurban'),('Urban','Urban')])


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@example.com'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username123'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
