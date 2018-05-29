from django.conf import settings

class custom_router:
    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASE_APPS_MAPPING:
            return  settings.DATABASE_APPS_MAPPING.get(app_label)
        return None

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASE_APPS_MAPPING:
            return settings.DATABASE_APPS_MAPPING.get(app_label)
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'auth' or \
                obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in settings.DATABASE_APPS_MAPPING:
            if db in settings.DATABASE_APPS_MAPPING.values():
                return settings.DATABASE_APPS_MAPPING.get(app_label) == db
            else:
                return False
        return None

