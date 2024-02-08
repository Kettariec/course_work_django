from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from datetime import datetime, timedelta
from newsletter.models import NewsLetter, Log


def send_letter():
    """Функция отправки сообщения списку клиентов"""
    day = timedelta(days=1, hours=0, minutes=0)
    weak = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    newsletter = list(NewsLetter.objects.all().filter(status='started'))

    for news in newsletter:

        if news.periodicity == 'one time':
            if news.date_time.strftime('%Y-%m-%d %H:%M') == now:

                newsletter_list = [client.mail for client in news.client.all()]

                result = send_mail(
                    subject=news.message.title,
                    message=news.message.text,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=newsletter_list,
                    fail_silently=False,
                )

                if result == 1:
                    status = 'Отправлено'
                else:
                    status = 'Ошибка отправки'
                print(status)

                log = Log(newsletter=news, status=status, user=news.user)
                log.save()

        else:
            if (news.next_date.strftime('%Y-%m-%d %H:%M') == now
                    or news.start_date.strftime('%Y-%m-%d %H:%M') == now):

                newsletter_list = [client.mail for client in news.client.all()]

                result = send_mail(
                    subject=news.message.title,
                    message=news.message.text,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=newsletter_list,
                    fail_silently=False,
                )

                if result == 1:
                    status = 'Отправлено'
                else:
                    status = 'Ошибка отправки'
                print(status)

                log = Log(newsletter=news, status=status, user=news.user)
                log.save()

                if news.periodicity == 'day':
                    news.next_date = log.date_time + day
                elif news.periodicity == 'week':
                    news.next_date = log.date_time + weak
                elif news.periodicity == 'month':
                    news.next_date = log.date_time + month

                if (news.next_date.strftime('%Y-%m-%d %H:%M') >
                        news.end_date.strftime('%Y-%m-%d %H:%M')):
                    news.status = 'completed'
                news.save()
