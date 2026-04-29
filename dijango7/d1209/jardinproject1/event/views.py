from django.shortcuts import render

def write(request):
    return render(request, 'event_write.html')
