from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from . import forms
from .models import SensorsData, LocationData
from cloudant.client import CouchDB
from cloudant.result import Result, ResultByKey
import googlemaps
#from django_filters import rest_framework as filters

#connecting CouchDB
SERVER = CouchDB('admin', 'groupproject', url='http://localhost:5984', connect=True)
if len(SERVER) == 0:
    SERVER.create_database('docs')


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):
        form = forms.HomeForm()

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = forms.HomeForm(request.POST)
        if form.is_valid():
            form.save()
            db = SERVER['docs']
            doc = form.cleaned_data
            db.create_document(doc)
            return render(request, self.template_name, {'form': form})


class DetailView(TemplateView):
    template_name = "home/details.html"

    def get(self, request):
        # if not request.user.is_authenticated:
        #     return redirect_to_login(reverse('details'))
        # else:
        form = forms.DetailForm()
        args = {'form': form}
        return render(request, self.template_name, args)


    def post(self, request):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['ID']

            try:
                data = SensorsData.objects.get(pk=num)
            except:
                data = SensorsData()
                # raise Http404

        return render(request, self.template_name, {'form': form, 'data': data})


class MapView(TemplateView):
    template_name = "home/map.html"

    def get(self, request):
        form = forms.MapForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.MapForm(request.POST)

        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            return render(request, self.template_name, {'form': form, 'latitude': latitude, 'longitude': longitude})


class Checking(TemplateView):
    template_name = "home/checking.html"

    def get(self, request):
        form_add = forms.CheckingAddForm()
        form_check = forms.CheckingForm()
        try:
            data = LocationData.objects.all()
        except:
            data = LocationData()
            # raise Http404

        args = {'data':data, 'form_add':form_add, 'form_check':form_check}
        return render(request, self.template_name, args)

    def post(self, request):
        form_add = forms.CheckingAddForm(request.POST)
        form_check = forms.CheckingForm(request.POST)

        if form_add.is_valid():
            form_add.save()

        if form_check.is_valid():
            location = form_check.cleaned_data['location']
            latitude = location.lat
            longitude = location.long
            gmaps = googlemaps.Client('AIzaSyBLjb0Uy0iwnBrPZlAZnyl78jjPQ93w5oU')
            reverse_geocode_result = gmaps.reverse_geocode((latitude,longitude))

        try:
            data = LocationData.objects.all()
        except:
            data = LocationData()
            # raise Http404

        args = {'data':data, 'form_add': form_add, 'form_check': form_check, 'latitude': latitude, 'longitude': longitude, 'reverse_geocode_result': reverse_geocode_result}
        return render(request, self.template_name, args)


class json_response(TemplateView):
    def get(self, request, id):
        try:
            data = SensorsData.objects.get(pk=id)
            json = serializers.serialize("json", [data])
        except:
            data = SensorsData()
            json = serializers.serialize("json", [data])

        return JsonResponse(json, safe=False)

