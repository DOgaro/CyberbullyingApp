from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'bullying'

urlpatterns = [
    url(r'^$', views.choose_bullying, name="choose_bullying"),
]
