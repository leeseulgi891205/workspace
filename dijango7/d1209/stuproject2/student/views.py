from django.shortcuts import render

def list(request):
    return render(request, 'student_list.html')

def write(request):
    return render(request, 'student_write.html')
