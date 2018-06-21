from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all_doctors', views.all_doctors, name='all_doctors'),
    url(r'^xsml_all_doctors', views.xsml_all_doctors, name='xsml_all_doctors'),
]
