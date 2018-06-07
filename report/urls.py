from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all_doctors', views.all_doctors, name='all_doctors'),
    url(r'^category_report/(?P<categorys>.+)', views.category_report, name='category_report'),
    url(r'^xsml_all_doctors', views.xsml_all_doctors, name='xsml_all_doctors'),
    url(r'^xsml_category/(?P<categorys>.+)', views.xsml_category, name='xsml_category'),
]
