from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to='media/',
                              verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='дата создания')
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             default=1, verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
