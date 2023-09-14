from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_item


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product/', create_product, name='create_product'),
    path('show_xml/', show_xml, name='show_xml'),
    path('show_json/', show_json, name='show_json'),
    path('show_xml_by_id/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('show_json_by_id/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
]