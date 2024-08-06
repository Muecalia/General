from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('country_list', v.CountryView.as_view(), name='country_list'),
    path('province_list', v.ProvinceView.as_view(), name='province_list'),
    path('county_list', v.CountyView.as_view(), name='county_list'),
]
