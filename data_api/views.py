from django.http import HttpResponse
from django.shortcuts import render

from data_api.models import Test


# Create your views here.

def orm_test(request):
    data = Test.objects.all()
    print(data)
    return HttpResponse("Hello, world. You're at the polls index.")