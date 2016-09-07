from django.conf.urls import url
from rango import views

urlpatterns=[
url(r'^$',views.rangoo, name='rangoo'),
url(r'^about/$',views.about,name="abt"),

]
