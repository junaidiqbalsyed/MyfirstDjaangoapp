from django.shortcuts import render

def employee (request):
    return render(request,
    'testapp/index.html')
