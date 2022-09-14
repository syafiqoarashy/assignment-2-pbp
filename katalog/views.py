from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_item': data_katalog_item,
        'name': 'Syafiqo Arashy Octaviano',
        'studentid': '2106657821'
    }
    return render(request, 'katalog.html', context)