import os

import yagmail
from celery import Celery
from yagmail import SMTP

yag = SMTP(os.getenv("EMAIL_HOST_USER"), os.getenv("EMAIL_HOST_PASSWORD"))

# language=html
EMAIL_TXT = """
<div>You have registered to FastAPI example</div>
<div>
    <a>This link does nothing</a>
</div>
""".strip()

celery_app = Celery('hello', broker='redis://redis-server:6379')


# this will send email to owner when any account is created (just to try celery with redis with yagmail)
@celery_app.task
def send_email(to: str, subject: str):
    yag.send(to, subject=subject, contents=EMAIL_TXT)
