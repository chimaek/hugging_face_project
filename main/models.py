from django.db import models
from django.conf import settings

DATA_API_KEY = settings.DATA_API_KEY


# Create your models here.
class KmoocRequest():
    def __init__(self, page):
        self.ServiceKey = DATA_API_KEY
        self.page = page
