from django.conf.urls import url
from django.urls import path
from . import views
app_name='work_history'
urlpatterns=[
path('',views.index1,name='index'),
];
