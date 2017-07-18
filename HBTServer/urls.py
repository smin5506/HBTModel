from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),
	url(r'^setdata/', views.setData),
	url(r'^viewdata/', views.viewData),
	url(r'^searchdata/(?P<mType>.+);(?P<mySearchData>.*);', views.searchData),
]
