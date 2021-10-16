import requests
from dani_shop.celery import app
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@app.task(queue=settings.CELERY_QUEUE)
def ask_to_telegram(question, email, topic):
    text = f'Mensaje de: {email}\nTopic: {topic}\n{question}'
    url = f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage?chat_id={settings.TELEGRAM_CHAT_ID}&text={text}'

    req = requests.post(url)

    if req.status_code >= 300:
        raise Exception(req.content)


@app.task(queue=settings.CELERY_QUEUE)
def ask_to_email(question, email, topic):
    subject, from_email = f'Consulta de {topic}', settings.EMAIL_HOST_USER

    with get_connection() as connection: # uses SMTP server specified in settings.py
        html_content = render_to_string('emails/ask_email.html', {'email': email, 'question': question})

        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [settings.EMAIL_TO_ASSISTANCE, ])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
