import requests
from django.http import HttpResponse
from django.shortcuts import render
from .models import JejuValuePlace
from data_api.models import Test
from django.conf import settings

DATA_API_KEY = settings.DATA_API_KEY


# Create your views here.

def orm_test(request):
    data = Test.objects.all()
    print(data)
    return HttpResponse("Hello, world. You're at the polls index.")


def call_api(request):
    # 쿼리 파라미터 방식
    page_no = int(request.GET.get("pageNo", 1))

    # api 요청
    url_base = f"http://apis.data.go.kr/6510000/goodPriceStoreService/getGoodPirceStoreList?ServiceKey={DATA_API_KEY}"

    if page_no > 1:
        url_base += f"&pageNo={page_no}"

    res_data = requests.get(url_base)

    # 안티패턴
    if not res_data.status_code == 200 or page_no < 1:
        return render(request, "error_500.html")

    api_data = res_data.json()

    total_page = api_data['response']['body']['totalCount']
    page_no = api_data['response']['body']['pageNo']
    items = api_data['response']['body']['items']['item']

    data = {
        "total_page": total_page,
        "page_no": page_no,
        "items": items
    }
    for v in items:
        if not JejuValuePlace.objects.filter(bsshNm=v['bsshNm']).exists():
            JejuValuePlace.objects.create(
                emdNM=v['emdNm'],
                bsshNm=v['bsshNm'],
                indutyNm=v['indutyNm'],
                rnAdres=v['rnAdres'],
                bsshTelno=v['bsshTelno'],
                prdlstCn=v['prdlstCn'],
                etcCn=v['etcCn'],
                regDt=v['regDt'],
                laCrdnt=v['laCrdnt'],
                loCrdnt=v['loCrdnt'],
                dataCd=v['dataCd'],
                slctnYr=v['slctnYr'],
                slctnMm=v['slctnMm'],
            )

    return render(request, "index.html", {"data": data})
