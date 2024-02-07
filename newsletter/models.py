from django.db import models
from django.conf import settings
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


PERIODICITY_CHOICES = (
    ('one time', 'разовая'),
    ('day', 'Раз в день'),
    ('week', 'Раз в неделю'),
    ('month', 'Раз в месяц'),
)

STATUS_CHOICES = (
    ('created', 'Создана'),
    ('started', 'Запущена'),
    ('completed', 'Завершена'),
)


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    mail = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name} ({self.mail})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    text = models.TextField(verbose_name='содержание')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class NewsLetter(models.Model):
    name = models.CharField(verbose_name="название", max_length=50)
    date_time = models.DateTimeField(default=timezone.now, verbose_name="дата и время для разовых", **NULLABLE)
    start_date = models.DateTimeField(default=timezone.now, verbose_name="начало периода", **NULLABLE)
    next_date = models.DateTimeField(default=timezone.now, verbose_name="следующая отправка")
    end_date = models.DateTimeField(default=timezone.now, verbose_name="конец периода", **NULLABLE)
    periodicity = models.CharField(default='one time', max_length=50,
                                   verbose_name="периодичность", choices=PERIODICITY_CHOICES)
    client = models.ManyToManyField(Client, verbose_name='клиент')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created', verbose_name='статус')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    permissions = [
        (
            'set_status',
            'Can change status'
        )
    ]


class Log(models.Model):
    newsletter = models.ForeignKey('NewsLetter', on_delete=models.CASCADE,
                                   verbose_name='рассылка', **NULLABLE)
    date_time = models.DateTimeField(default=timezone.now, verbose_name="время последней рассылки", **NULLABLE)
    status = models.CharField(max_length=150, verbose_name='статус отправки', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'Отправлено: {self.time},{self.date} ' \
               f'Статус: {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
