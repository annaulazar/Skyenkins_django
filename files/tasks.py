import subprocess
from celery import shared_task
from django.core.mail import send_mail

from Skyenkins_django.settings import EMAIL_HOST_USER
from .models import File, Logs


@shared_task
def verify_file():
    files = File.objects.filter(status__in=['new', 'updated'])
    for file in files:
        log_text = subprocess.run(['flake8', file.file.path], stdout=subprocess.PIPE).stdout.decode('utf-8')
        try:
            log = Logs.objects.get(file=file)
            log.logs = log_text
            log.save()
        except:
            Logs.objects.create(file=file, logs=log_text)

        file.status = File.VERIFIED
        file.save()

        send_log_email.delay(file.id)


@shared_task
def send_log_email(file_pk):
    log = Logs.objects.get(file_id=file_pk)
    log.send_mail = 1
    log.save()

    send_mail(
        'Проверка файла',
        'Проверка файла произведена.\n Результаты проверки:\n'
        f'{log.logs}',
        f'{EMAIL_HOST_USER}',
        [log.file.owner.email]
    )
