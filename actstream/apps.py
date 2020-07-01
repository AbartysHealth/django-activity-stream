import json
from datetime import datetime, time
from uuid import UUID

from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured

from actstream import settings
from actstream.signals import action


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return str(obj)

        if isinstance(obj, datetime):
            return str(obj)

        if isinstance(obj, time):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class ActstreamConfig(AppConfig):
    name = 'actstream'

    def ready(self):
        from actstream.actions import action_handler
        action.connect(action_handler, dispatch_uid='actstream.models')
        action_class = self.get_model('action')

        if settings.USE_JSONFIELD:
            try:
                from django_mysql.models import JSONField
                from jsonfield_compat import register_app
            except ImportError:
                raise ImproperlyConfigured(
                    'You must have django-jsonfield and django-jsonfield-compat '
                    'installed if you wish to use a JSONField on your actions'
                )
            JSONField(blank=True, null=True, encoder=CustomEncoder(allow_nan=False)).contribute_to_class(action_class, 'data')
            register_app(self)
