from flask import Flask

def init_app(app:Flask):
    from app.views.user_views import bp_user
    app.register_blueprint(bp_user)

    from app.views.megasena_views import bp_megasena
    app.register_blueprint(bp_megasena)