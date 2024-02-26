from django.shortcuts import render
from django.http import HttpResponse
from.models import Place, Place1


def demo(request):
    obj = Place.objects.all()
    obj1 = Place1.objects.all()
    return render(request,'index.html',{'result': obj,'result1':obj1})
    obj1= Place1.objects.all()






























# Create your views here.
# def demo(request):
#     return render(request,"homme.html")
#
#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET["num2"])
#     sum=x+y
#     sub=x-y
#     div=x/y
#     mul=x*y
#
#     return render(request,"result.html",{'result':sum,'subtraction':sub,'division':div,'product':mul})
