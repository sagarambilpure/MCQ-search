from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter_ques', views.filter_ques, name='filter_ques'),

]
