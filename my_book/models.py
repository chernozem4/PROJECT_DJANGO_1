from django.db import models




class MyBook(models.Model):
    GENRES = [
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=250, verbose_name='Название', null=True, db_index=True)
    author = models.CharField(max_length=250, verbose_name='Автор', null=True, db_index=True)
    image = models.ImageField(upload_to='book/', verbose_name='Вид', null=True, db_index=True)
    description = models.TextField(verbose_name='Описание', null=True, db_index=True)
    genre = models.CharField(max_length=50, choices=GENRES, verbose_name='Жанр', null=True, db_index=True)

    def __str__(self):
        return f'{self.title} - {self.genre}'






