from django.shortcuts import render, HttpResponse
from .models import Foodbanks, Shelters, Pharmacy, Hospitals, CampingAreas, DrugTesting, DetoxCentre, SafeConsumptionSite

def foodbanks(request): 
  banks = Foodbanks.objects.all()
  return (request, {'foodbanks': banks})

def safeconsumptionsites(request):
  sites = SafeConsumptionSite.objects.all()
  return (request, {'safeconsumptionsites': sites})

def shelters(request):
  facilities = Shelters.objects.all()
  return (request, {'shelters': facilities})