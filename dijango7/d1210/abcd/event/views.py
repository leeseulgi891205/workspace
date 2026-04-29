from django.shortcuts import render

def index(request):
    return render(request, 'event_index.html')

def write(request):
    return render(request, 'event_write.html')
