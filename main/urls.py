from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id,\
                        show_json_by_id, delete_item, register, login_user, logout_user, get_product_json, \
                        add_product_ajax, delete_item_ajax, increment_item_ajax, decrement_item_ajax, create_item_flutter



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product/', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('increment-item-ajax/<int:id>/', increment_item_ajax, name='increment_item_ajax'),
    path('decrement-item-ajax/<int:id>/', decrement_item_ajax, name='decrement_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]