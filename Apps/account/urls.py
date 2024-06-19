from django.urls import path

from apps.account import views

urlpatterns = [
    path('',views.users,name='users')
]
