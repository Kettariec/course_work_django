from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    mail = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.mail})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    text = models.TextField(verbose_name='содержание')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='владелец рассылки')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
