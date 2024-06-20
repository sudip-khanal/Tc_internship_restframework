from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from apps.account.models import *
from apps.account.serializers import *
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()
## User API ##

@api_view(['GET'])
def users(self):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(self,pk):
    user = get_object_or_404(User,pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(self,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return Response(status=status.HTTP_200_OK)



### Author API #####

@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_author(self,pk):
    author=get_object_or_404(Author,pk=pk)
    serializer=AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['GET'])
def authors(self):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_author(self,pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return Response(status=status.HTTP_200_OK)


## Book API ##
@api_view(['POST'])
def create_book(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def books(self):
    books = Author.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book(self,pk):
    book = get_object_or_404(Book,pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

def delete_book(self,pk):
    book = get_object_or_404(Book,pk=pk)
    book.delete()
    return Response(status=status.HTTP_200_OK)


