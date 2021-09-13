from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('courses/create', views.create_course),
]