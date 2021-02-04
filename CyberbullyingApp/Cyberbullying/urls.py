from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Cyberbullying'

urlpatterns = [
    url(r'^$', views.Cyberbullying_analysis, name="Cyberbullying_analysis"),
    url(r'^type/$', views.Cyberbullying_analysis_type, name="Cyberbullying_analysis_type"),
    url(r'^import/$', views.Cyberbullying_analysis_import, name="Cyberbullying_analysis_import"),
]
