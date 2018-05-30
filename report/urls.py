from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all_doctors', views.index, name='all_doctors'),
]
