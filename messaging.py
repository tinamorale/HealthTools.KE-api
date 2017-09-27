from celery import Celery

from healthtools_ke_api.settings import CLOUDAMQP_URL

celery_app = Celery('estasks', backend='amqp', broker=CLOUDAMQP_URL)


@celery_app.task
def print_hello():
    print "hello there"