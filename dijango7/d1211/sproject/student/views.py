from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        hobby = request.POST.get('hobby')
        
        Student.objects.create(
            name=name,
            major=major,
            age=age,
            grade=grade,
            gender=gender,
            address=address,
            hobby=hobby
        )
        
        return redirect('/student/')
    
    return render(request, 'student/write.html')

def list(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})

def view(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student/view.html', {'student': student})

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/student/list/')

def update(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student/update.html', {'student': student})

def update_process(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        student.name = request.POST.get('name')
        student.major = request.POST.get('major')
        student.age = request.POST.get('age')
        student.grade = request.POST.get('grade')
        student.gender = request.POST.get('gender')
        student.address = request.POST.get('address')
        student.hobby = request.POST.get('hobby')
        student.save()
        
        return redirect('/student/view/' + str(id) + '/')
    
    return redirect('/student/list/')
