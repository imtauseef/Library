from email.policy import default
from tkinter import Image
from django.db import models
from django.forms import ImageField

# Create your models here.
class LibraryGallery(models.Model):
    gallery = models.CharField(max_length=100)


class Section(models.Model):
    section_gallary = models.ForeignKey(LibraryGallery, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=150)
    total_book_space = models.CharField(max_length=100)


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_books = models.OneToOneField(max_length=100, on_delete=models.CASCADE)


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    book_lang = models.CharField(max_length=100)
    book_code = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to="mylibrary/static/mylibrary")


class Reader(models.Model):
    reader_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)
    book = models.ManyToManyField(Book, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now_add=True)
    

