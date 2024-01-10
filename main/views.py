import requests
from django.shortcuts import render
from django.conf import settings
from requests import Request

DATA_API_KEY = settings.DATA_API_KEY


def index(request):
    data = requests.get(
        f"http://apis.data.go.kr/6510000/goodPriceStoreService/getGoodPirceStoreList?ServiceKey={DATA_API_KEY}")
    print(data.json())
    return render(request, "index.html", {"DATA_API_KEY": data.json()})

# Create your views here.
