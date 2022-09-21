from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_data_xml
from mywatchlist.views import show_data_json
from mywatchlist.views import show_data_xml_id
from mywatchlist.views import show_data_json_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_data_xml, name='show_html'),
    path('xml/', show_data_xml, name='show_xml'),
    path('json/', show_data_json, name='show_json'),
    path('json/<int:id>', show_data_json_id, name='show_data_jason_id'),
    path('xml/<int:id>', show_data_xml_id, name='show_data_xml_id'),
]