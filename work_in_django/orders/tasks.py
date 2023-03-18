from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):

    """Задача отправки email-уведомлений при успешном оформлении заказа."""

    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа. {}'.format(order.id)
    message = 'Dear {},\n\n Вы успешно разместили заказ.\
    Номер вашего заказа {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message,
                          'reis_969@mail.ru', [order.email])
    return mail_sent
