from django.urls import path
from . import views
urlpatterns =[
    path('test', views.orm_test, name='orm_test'),
    path('data', views.call_api, name='call_api'),
]