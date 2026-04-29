from django.shortcuts import render, redirect
from .models import Student

def index(request):
    return render(request, 'index.html')

def list(request):
    qs = Student.objects.all()
    context = {'list': qs}
    return render(request, 'student/list.html', context)

def write(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        hobby = request.POST.get('hobby')
        
        Student.objects.create(
            user_id=user_id,
            password=password,
            name=name,
            nickname=nickname,
            email=email,
            phone=phone,
            gender=gender,
            age=age,
            grade=grade,
            hobby=hobby
        )
        return redirect('/student/list/')
    
    return render(request, 'student/write.html')

def view(request, sno):
    student = Student.objects.get(sno=sno)
    context = {'student': student}
    return render(request, 'student/view.html', context)
