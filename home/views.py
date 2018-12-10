from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, Http404
from . import forms
from .models import SensorsData
from cloudant.client import CouchDB
from cloudant.result import Result, ResultByKey

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
        form = forms.DetailForm()
        db = SERVER['docs']
        docs = Result(db.all_docs, include_docs=True)
        args = {'form': form, 'docs': docs }
        return render(request, self.template_name, args)

    def post(self, request):
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['ID']
            print(num)

            try:
                data = SensorsData.objects.get(pk=num)
            except:
                data = SensorsData()
                # raise Http404

            return render(request, self.template_name, {'form': form, 'data': data})



