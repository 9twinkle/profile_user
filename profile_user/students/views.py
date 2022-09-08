
from django.shortcuts import render
from django.http import HttpResponse
from students.models import Register

def index(request):
     return render(request,'Register.html')

def submit_form(request):
    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Email_Id=request.POST['Email_Id']
        Department_Name=request.POST['Department_Name']
        Section_Name=request.POST['Section_Name']
        Phone_Number=request.POST['Phone_Number']
        Roll_Number=request.POST['Roll_Number']

        print(First_Name,Last_Name,Email_Id,Department_Name,Section_Name,Phone_Number,Roll_Number)
        Register(First_Name, Last_Name, Email_Id,Department_Name, Section_Name, Phone_Number, Roll_Number).save() 
        msg="form Submitted Successfuly"
        return render(request, 'Register.html',{'msg':msg})
    else:
      return HttpResponse("<h1>404 Not Found</h1>")





 





