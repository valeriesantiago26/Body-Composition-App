from django import forms
from .models import Person, Measurements


class PersonalInfoForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'

	firstName = forms.CharField(label="First Name:", required=True, 
		widget=forms.TextInput(attrs={'class': "form-control"}))

	lastName = forms.CharField(label="Last Name:", required=True, 
    	widget=forms.TextInput(attrs={'class': "form-control"}))

	DOB = forms.DateField(label="Date of Birth:", widget=forms.SelectDateWidget(
		empty_label=("Choose Year", "Choose Month", "Choose Day"), 
		attrs={'class': "form-control"}))

	gender = forms.ChoiceField(label="Gender:", 
		widget=forms.RadioSelect(attrs={'class': "form-check-input"}), 
		choices=Person.Gender.choices)
