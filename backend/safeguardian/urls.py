from django.urls import path, HttpResponse
from . import views


urlpatterns = [
  path('foodbanks', views.foodbanks, name='foodbanks'),
  path('shelters', views.shelters, name='shelters'),
  path('pharmacy', views.pharmacy, name='pharmacy'),
  path('safe_consumption_sites', views.safe_consumption_sites, name='safe_consumption_sites'),
  path('hospitals', views.hospitals, name='hospitals'),
  path('camping_areas', views.camping_areas, name='camping_areas'),
  path('drug_testing', views.drug_testing, name='drug_testing'),
  path('detox_centre', views.detox_centre, name='detox_centre'),
]