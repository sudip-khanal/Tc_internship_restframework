from django.urls import path

from apps.account import views

urlpatterns = [
    path('users/',views.users,name='users'),
    path('get_user/<int:pk>',views.get_user,name='get_user'),
    path('create_user/',views.create_user,name='create_user'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),

    path('create_author/',views.create_author,name='create_author'),
    path('authors/',views.authors,name='authors'),
    path('get_author/<int:pk>',views.get_author,name='get_author'),
    path('delete_author/<int:pk>',views.delete_author,name='delete_author'),

    path('create_book/',views.create_book,name='create_book'),
    path('books/',views.books,name='books'),
    path('get_book/<int:pk>',views.get_book,name='get_book'),
    path('delete_book/<int:pk>',views.delete_book,name='delete_book'),

]
