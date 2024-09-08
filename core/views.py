from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import scheduleAppointment, Doctor, Billing, Patient, Care
# Create your views here.

def home(request):
    return render(request, 'winers.html', {})

def treatment_care(request):
    return render(request, 'care.html', {})

def make_appointment(request):

    doctors = Doctor.objects.all()
    
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        doctor_name = request.POST['doctor_name']

        new_appointment = scheduleAppointment.objects.create(patient_name=patient_name, appointment_date=appointment_date, appointment_time=appointment_time, doctor_name=doctor_name)

        new_appointment.save()

        messages.info(request, 'Appointment added Successfully!')
        return redirect('/')

    else:

        return render(request, 'scheduling.html', {'doctors':doctors})


def billing(request):
    payments = Billing.objects.all()
    if request.method == 'POST':

        patient_name = request.POST['name']
        amount = request.POST['amount']

        new_payment = Billing.objects.create(name=patient_name, amount=amount)
        new_payment.save()
        messages.info(request, 'payment Successfully!')
        return redirect('billing')
    else:
        return render(request, 'bill.html', {'payments': payments})

# def employee(request):
#    return render(request, 'EMPLOYEE.html', {'payments': payments})



def Logout(request):
   logout(request)
   return redirect('Login')

def patient(request):

    if request.method == 'POST':
        name = request.POST['patient-name']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        medical_history = request.POST['medical-history']
        
        new_patient = Patient.objects.create(name=name, age=age, sex=gender, address=address, phone=phone, email=email, medical_history=medical_history)
        new_patient.save()
        messages.info(request, 'New patient added successfully!')
        return redirect('patient')
    else:
        return render(request, 'PATIENT.html')


def medical_records(request):
    patients =Patient.objects.all()

    return render(request, 'records.html', {'patients':patients})


def care(request): 
    if request.method == 'POST':

        name = request.POST['name']
        treatment_plan = request.POST['plan']
        care_status= request.POST['status']
        care_notes = request.POST['notes']

        new_care = Care.objects.create(patient_name=name,treatment_plan=treatment_plan,care_status=care_status, care_notes=care_notes )
        new_care.save()
        return redirect('care')
    else:
        return render(request, 'care.html', {})