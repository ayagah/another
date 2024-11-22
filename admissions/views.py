from django.shortcuts import render,redirect,get_object_or_404
from.models import patient
from django.forms import patientForm


def Patient(request):
    if request.method=="POST":
        Form=patientForm(request.POST)
    if Form.is_valid():
        Form.save()
        return redirect("patient_list")
    else:
       Form=patientForm()
    return render(request,"admission/patient_list.html")
        

# Create your views here.
