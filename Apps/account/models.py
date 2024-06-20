
# from django.db import models
# from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
]

# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     bio = models.TextField(max_length=500, blank=True)
#     phone_number = models.CharField(max_length=15, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

#     def __str__(self):
#         return self.username


# class Author(models.Model):
#     name=models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    favorite_authors = models.ManyToManyField('Author', blank=True)

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey(Author,related_name='book', on_delete=models.CASCADE)
    isbn_number=models.IntegerField()
    pages=models.IntegerField()

    def __str__(self):
        return  f"{self.name} {self.author}"
