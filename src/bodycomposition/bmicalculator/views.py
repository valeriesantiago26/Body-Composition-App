from django.shortcuts import render
from .forms import PersonalInfoForm
from . import helperfunctions

# Home Page
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

# bmi Page
def bmi_view(request, *args, **kwargs):
	return render(request, "bmi.html", {})

# body composition Page
def bodyComp_view(request, *args, **kwargs):
	return render(request, "bodycomp.html", {})

# Personal Information Page
def info_view(request, *args, **kwargs):
	if request.method == "POST":
		form = PersonalInfoForm(request.POST or None)
		#print(form['firstName'].value())

		if form.is_valid():
			#form.save()
			print("Save")
			return render(request, "bmi.html", {})

	else:
		form = PersonalInfoForm()

	form.isValid = form.is_valid()
  
	context = {'form': form }
	return render(request, "info.html", context)