import os

from flask import Flask
from celery import Celery

from downloader import error_handler, my_downloader
from flask_cors import CORS


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//',
        CELERY_RESULT_BACKEND = 'rpc://' 
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.register_blueprint(error_handler.bp)
    app.register_blueprint(my_downloader.bp, url_prefic='/')
    app.add_url_rule('/', endpoint='index')
    # app.add_url_rule('/download/<filename>', endpoint='download')z

    return app


app = create_app()
celery = make_celery(app)