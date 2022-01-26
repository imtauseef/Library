from django.contrib import admin
from .models import LibraryGallery, Section, Author, Book, Reader
# Register your models here.

admin.site.register(LibraryGallery)
admin.site.register(Section)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Book)