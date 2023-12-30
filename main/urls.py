from django.urls import path

from main import views

urlpatterns = [
    path('index', views.homepage, name='index'),
    path("test",views.test, name='test'),
]