from django.shortcuts import render
import datetime


# Create your views here.

def homepage(request):
    current_time = datetime.datetime.now()  # 현재 날짜 구하기
    context = {
        'comma': 50000,
        'word': 180000000000,
        'current_time': current_time,
        "number1": 10,
        "number2": 1,
        "yesterday": current_time - datetime.timedelta(days=1),
        "tomorrow": current_time + datetime.timedelta(days=1),
    }
    return render(request, 'human.html', context)
# views.py
from django.shortcuts import render
def test(request):
	context ={"name" : "홍길동", "age" : 40}

	return render(request,"test.html", context)