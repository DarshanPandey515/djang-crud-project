from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def index(request):
    students = Student.objects.all()
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def adddata(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            sname = form.cleaned_data['Student_Name']
            sclass = form.cleaned_data['Student_Class']
            ssection = form.cleaned_data['Student_Section']
            sage = form.cleaned_data['Student_Age']
            ssex = form.cleaned_data['Student_Sex']
            reg = Student(Student_Name=sname,Student_Class=sclass,Student_Section=ssection,Student_Age=sage,Student_Sex=ssex)
            reg.save()
            messages.success(request, 'Student Registered Successfully !')

            return redirect('index')
    else:
        form = StudentForm()
    return render(request,'adddata.html',{'form':form})



def deletestudent(request, id):
    student = Student.objects.get(Student_ID=id)
    student.delete()
    messages.success(request, 'Student Deleted Successfully !')
    return redirect('index')


def edit(request , id):
    if request.method == 'POST':
        student = Student.objects.get(Student_ID=id)
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Updated Successfully !')
            return redirect('index')
    else:
        student = Student.objects.get(Student_ID=id)
        form = StudentForm(instance=student)
    return render(request,'update_student.html',{'form':form})

def search(request):
    query = request.GET['query']
    stddata = Student.objects.filter(Q(Student_Name__icontains=query) | Q(Student_Class__icontains=query) | Q(Student_Section__icontains=query) | Q(Student_Age__icontains=query))
    context = {
        'stddata':stddata,
        'query':query
    }
    return render(request,'search.html',context)