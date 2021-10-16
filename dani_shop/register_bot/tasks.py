from dani_shop.celery import app
from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@app.task(queue=settings.CELERY_QUEUE)
def send_welcome_email(email):
    subject, from_email = 'Welcome to Dani Shop', settings.EMAIL_HOST_USER

    with get_connection() as connection: # uses SMTP server specified in settings.py
        html_content = render_to_string('emails/welcome_email.html', {})

        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [email, ])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
