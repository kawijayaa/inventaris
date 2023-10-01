from django.urls import path
from main.views import show_main, create_product, delete_product, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, increment_amount, decrement_amount, edit_product

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', show_products, name='show_products'),
    path('products/create/', create_product, name='create_product'),
    path('products/delete/<int:id>/', delete_product, name='delete_product'),
    path('products/xml/', show_xml, name='show_xml'),
    path('products/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('products/json/', show_json, name='show_json'),
    path('products/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/increment/<int:id>/', increment_amount, name='increment_amount'),
    path('products/decrement/<int:id>/', decrement_amount, name='decrement_amount'),
    path('products/edit/<int:id>/', edit_product, name='edit_product')
]