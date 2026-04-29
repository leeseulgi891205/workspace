from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Student


def list(request):
    qs = Student.objects.all().order_by('-name')
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student/list.html', context)

# 학생등록페이지 및 등록처리
def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        address = request.POST.get('address', '')
        
        # Student 모델에 데이터 저장
        Student.objects.create(
            name=name,
            major=major,
            age=age,
            grade=grade,
            address=address)
        
        return redirect('/student/list/')
    
    return render(request, 'student/write.html')

def view(request, sno):
    student = get_object_or_404(Student, pk=sno)
    context = {'student': student}
    return render(request, 'student/view.html', context)

# 학생수정페이지 및 수정처리
def update(request, sno):
    student = get_object_or_404(Student, pk=sno)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.major = request.POST.get('major')
        student.age = request.POST.get('age')
        student.grade = request.POST.get('grade')
        student.address = request.POST.get('address', '')
        student.save()
        
        return redirect('student:view', sno=sno)
    
    context = {'student': student}
    return render(request, 'student/update.html', context)

# 학생삭제페이지
def delete(request, sno):
    student = get_object_or_404(Student, pk=sno)
    student.delete() # 삭제
    return redirect('student:list')
