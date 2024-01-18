from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("predict/", views.predict, name="predict"),
    path("predict_image/", views.predict_image, name="predict_image"),
    path("image_result/", views.image_result, name="image_result"),
]
