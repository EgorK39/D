from pprint import pprint

from django.template.loader import render_to_string

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import (
    send_mail, mail_managers, EmailMultiAlternatives
)
from .models import PostModel, Comment


@receiver(post_save, sender=Comment)
def notify_comment(sender, instance, created, **kwargs):
    email = instance.post.author.email
    post = instance.post
    post_title = instance.post.title
    id_obj = instance.post.id

    html_content = render_to_string(
        'email/send_mail_comment.html',
        {
            'text': instance.text,
            'post_title': post_title,
            'id_obj': id_obj,
            'post': post,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Новый отклик!',
        body='',
        from_email='egor159kulikov@yandex.ru',
        to=[email],
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
