class BookRouter:
    """
    A router to control all database operations on models in the books application.
    """
    route_app_labels = {'books'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read books models go to mysql_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write books models go to mysql_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the books app is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the books app only appears in the 'mysql_db'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'mysql_db'
        return None
