# Generated by Django 4.0.1 on 2022-01-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('quantity_books_written', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_lang', models.CharField(max_length=100)),
                ('book_code', models.CharField(max_length=100)),
                ('book_image', models.ImageField(upload_to='mylibrary/static/mylibrary')),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.author')),
            ],
        ),
        migrations.CreateModel(
            name='LibraryGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=150)),
                ('total_book_space', models.CharField(max_length=100)),
                ('section_gallary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.librarygallery')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=100)),
                ('from_date', models.DateField(auto_now_add=True)),
                ('book', models.ManyToManyField(to='mylibrary.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.section'),
        ),
    ]
