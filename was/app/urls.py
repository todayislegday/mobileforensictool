#url 리졸버

from django.urls import path,re_path
from . import views

urlpatterns = [
    #대시보드 페이지
    path('', views.index, name='home'),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
