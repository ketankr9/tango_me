from django.conf.urls import url,include
from rango import views

urlpatterns=[
url(r'^$',views.rangoo, name='rangoo'),
url(r'^about/$',views.about,name="abt"),
#url(r'^static/',)

]
