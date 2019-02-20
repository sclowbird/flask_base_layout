from flask import Flask, render_template


#db = SQLAlchemy()

def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """  

    app = Flask(__name__)
    app.config.from_object(object_name)

    #db.init_app(app)

    from .main import create_module as main_create_module
    main_create_module(app)






    #app.register_blueprint(auth_blueprint)

    return app