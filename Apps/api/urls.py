from django.urls import path
from . import views
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('get_products/', views.get_products,name="get-all"),
    path('get_product/<int:pk>',views.get_product,name='get_product'),
    path('create_product/',views.create_product,name='create_product'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('update_product/<int:pk>',views.update_product,name='update_product'),

]
