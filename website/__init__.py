from flask import Flask


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["SECRET_KEY"] = "27493hd9fh03h9u4bv830tj9493jld02n4fy7.874nvocn393nuvy34f6cnHGDn8Bfinf"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
