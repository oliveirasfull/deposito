import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    template_dir = os.path.abspath('./src')
    app = Flask(
        __name__,
        template_folder=f'{template_dir}/templates',
        static_folder=f'{template_dir}/static'
    )
    app.config.from_object('config.Dev')

    db.init_app(app)
    migrate.init_app(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)


    '''Import models'''
    import src.models


    '''Import Blueprint'''
    from src.views import views
    views.configure(app)

    return app
