from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from cloudant.client import CouchDB

SERVER = CouchDB('admin', 'groupproject', url='http://localhost:5984', connect=True)
if len(SERVER) == 0:
    SERVER.create_database('docs')


# Create your views here.
#def index(request):
#    docs = SERVER['docs']
#    if request.method == 'POST':
#        title = request.POST['title'].replace(' ','')
#        docs[title] = {'title': title, 'text': ""}
#        return HttpResponseRedirect(u"/doc/%s" % title)
#    return render(request, "{% url 'index' %}", {})

class HomeView(TemplateView):
    template_name = 'home/index.html'



