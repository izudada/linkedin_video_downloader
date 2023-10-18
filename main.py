import os
import logging
import time

from celery import Celery

from downloader import create_app


app = create_app()

celery = Celery(
    app.import_name,
    broker=app.config['CELERY_BROKER_URL'],
    backend=app.config['CELERY_RESULT_BACKEND']
)
celery.conf.update(app.config)


if __name__ == '__main__':
    app.run(debug=True)