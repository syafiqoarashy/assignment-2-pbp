from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    context = {
        'name': 'Syafiqo Arashy Octaviano',
        'studentid': '2106657821',
        'list_item': data_mywatchlist_item,
    }
    return render(request, "mywatchlist.html", context)

def show_data_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_data_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_data_xml_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_data_json_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")