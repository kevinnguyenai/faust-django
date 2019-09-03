import os
import faust

# make sure the gevent event loop is used as early as possible.
os.environ.setdefault('FAUST_LOOP', 'eventlet')

# set the default Django settings module for the 'faust' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = faust.App('django-proj', autodiscover=True, 
    broker='kafka://172.16.0.20:9092', 
    origin='faustapp',
    value_serializer='json'
    )


@app.on_configured.connect
def configure_from_settings(app, conf, **kwargs):
    from django.conf import settings
    conf.broker = settings.FAUST_BROKER_URL
    conf.store = settings.FAUST_STORE_URL


def main():
    app.main()


if __name__ == '__main__':
    main()
