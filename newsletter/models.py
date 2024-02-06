from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


PERIODICITY_CHOICES = (
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
    # time = models.TimeField(verbose_name='время рассылки')
    # date = models.DateField(verbose_name='дата рассылки')
    # periodisity = models.CharField(max_length=20, choices=PERIODISITY_CHOISES,
    #                                default='created', verbose_name='статус рассылки')
    # client = models.ManyToManyField('Client', verbose_name='клиент')
    # message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='сообщение')
    # status = models.CharField(max_length=20, choices=STATUS_CHOISES,
    #                           default='created', verbose_name='статус рассылки')
    #
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    #                          default=1, verbose_name='пользователь')
    time = models.TimeField(verbose_name='время рассылки')
    date = models.DateField(verbose_name='дата рассылки')
    periodicity = models.CharField(default='разовая', max_length=50,
                                   verbose_name="периодичность", choices=PERIODICITY_CHOICES)
    client = models.ManyToManyField(Client, verbose_name='клиент')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created', verbose_name='статус')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.date} \n {self.message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    permissions = [
        (
            'set_status',
            'может изменять статус'
        )
    ]


class Log(models.Model):
    newsletter = models.ForeignKey('NewsLetter', on_delete=models.CASCADE,
                                   verbose_name='рассылка', **NULLABLE)
    time = models.DateField(auto_now_add=True, verbose_name='время последней попытки')
    status = models.CharField(max_length=150, verbose_name='статус отправки', **NULLABLE)
    # server_response = models.CharField(max_length=150, verbose_name='ответ сервера', **NULLABLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'Отправлено: {self.time}, ' \
               f'Статус: {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
