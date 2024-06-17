from .auth.auth import auth

bps = {
    auth: "/auth",
}


def register(app):
    for bp in bps:
        app.register_blueprint(bp, url_prefix=bps[bp])

