import os
from flask_admin import Admin
from models import db, User, Planet, Character, Vehicle, Favorite
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class NewModel(ModelView):
        column_display_pk = True

    admin.add_view(NewModel(User, db.session))
    admin.add_view(NewModel(Planet, db.session))
    admin.add_view(NewModel(Character, db.session))
    admin.add_view(NewModel(Vehicle, db.session))
    admin.add_view(NewModel(Favorite, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))