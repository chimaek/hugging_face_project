from django.db import models
from django.db.models import Model


# Create your models here.


class JejuValuePlace(models.Model):
    # 읍면동
    emdNM = models.CharField(max_length=100)
    # 업소 명
    bsshNm = models.CharField(max_length=200)
    # 업종 명
    indutyNm = models.CharField(max_length=200)
    # 도로명 주소
    rnAdres = models.CharField(max_length=200)
    # 업소 전화번호
    bsshTelno = models.CharField(max_length=200)
    # 품목 내용
    prdlstCn = models.CharField(max_length=200)
    # 기타 내용
    etcCn = models.CharField(max_length=200)
    # 등록 일시
    regDt = models.CharField(max_length=200)
    # 위도
    laCrdnt = models.CharField(max_length=200)
    # 경도
    loCrdnt = models.CharField(max_length=200)
    # 데이터 코드
    dataCd = models.CharField(max_length=200)
    # 선정 연도
    slctnYr = models.CharField(max_length=200)
    # 선정 월
    slctnMm = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.emdNM} {self.bsshNm} {self.indutyNm} {self.rnAdres} {self.bsshTelno} {self.prdlstCn} {self.etcCn} {self.regDt} {self.laCrdnt} {self.loCrdnt} {self.dataCd} {self.slctnYr} {self.slctnMm}"

    meta = {
        'db_table': 'jeju_value_place'
    }
