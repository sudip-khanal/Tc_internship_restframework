
from rest_framework import serializers
from .models import CustomUser, Author, Book
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ 'id','name']

class BookSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = [ 'name', 'isbn_number', 'pages','author_details']
        read_only_fields = ('created','updated')


    # def to_representation(self, instance):
    #     self.fields['book'] =  AuthorSerializer(read_only=True)
    #     return super(BookSerializer, self).to_representation(instance)
    
    
    
    def update(self, instance, validated_data):
        author = validated_data.pop('author')
        instance = super().update(instance, validated_data)

        # Clear current favorite authors
        instance.authors.clear()

        for author_data in author:
            author, created = Author.objects.get_or_create(**author_data)
            instance.authors.add(author)

        return instance


class UserSerializer(serializers.ModelSerializer):
    favorite_authors = AuthorSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'date_of_birth', 'bio', 'phone_number', 'address', 'gender', 
            'favorite_authors'
        ]

    def create(self, validated_data):
        favorite_authors = validated_data.pop('favorite_authors')
        user = User.objects.create(**validated_data)

        for author_data in favorite_authors:
            author, created = Author.objects.get_or_create(**author_data)
            author.name = "sudip"
            author.updated_fields['name']
            user.favorite_authors.add(author)
        return user

    def update(self, instance, validated_data):
        favorite_authors = validated_data.pop('favorite_authors')
        instance = super().update(instance, validated_data)

        # Clear current favorite authors
        instance.favorite_authors.clear()

        for author_data in favorite_authors:
            author, created = Author.objects.get_or_create(**author_data)
            instance.favorite_authors.add(author)

        return instance
