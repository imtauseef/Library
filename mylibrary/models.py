from email.policy import default
from tkinter import Image
from django.db import models
from django.forms import ImageField

# Create your models here.
class LibraryGallery(models.Model):
    gallery = models.CharField(max_length=100)

    def __str__(self):
        return self.gallery


class Section(models.Model):
    section_gallary = models.ForeignKey(LibraryGallery, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=150)
    total_book_space = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    quantity_books_written = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    book_lang = models.CharField(max_length=100)
    book_code = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to="mylibrary/static/mylibrary")

    def __str__(self):
        return self.book_name

class Reader(models.Model):
    reader_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)
    book = models.ManyToManyField(Book,)
    from_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.reader_name
