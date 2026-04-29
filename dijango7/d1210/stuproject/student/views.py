from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student

# 학생등록함수
def write(request):
    if request.method == 'GET':
        return render(request, 'student/write.html')
    elif request.method == 'POST':
        # form폼에서 넘어온 데이터 처리
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        # hobbys = ",".join(hobby) # 리스트를 문자열로 변환
        # 리스트타입을 문자열항목에 저장하면 자동으로 형 변환됨.
        
        # qs = Student(name=name, age=age, grade=grade, gender=gender, hobby=hobby)
        # qs.save()
        Student.objects.create(name=name, age=age, grade=grade, gender=gender, hobby=hobby)
        
        # Student.objects.create(name=name, age=age, grade=grade, gender=gender)

        
        print("이름 : ", name)
        print("취미 : ", hobby)
        return redirect(reverse('student:list'))
    # return render(request, 'student/write.html')
    # return render(request, 'student/write.html')
    #return redirect('/')

# 학생리스트함수
def list(request):
    # DB에서 전체 레코드 가져오기
    # select, insert, update, delete
    
    qs = Student.objects.all().order_by('-sno','name')
    context = {"list":qs}
    return render(request, 'student/list.html', context)

def view(request, sno):
    print("넘어온 데이터 sno : ", sno)
    qs = Student.objects.get(sno=sno)
    context = {"student": qs}
    return render(request, 'student/view.html', context)




def delete(request):
    return render(request, 'student/delete.html')
