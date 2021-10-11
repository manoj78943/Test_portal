from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def test(request):
    return render(request,'Test.html')
def result(request):
    return render(request,'result.html')