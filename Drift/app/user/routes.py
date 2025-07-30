from flask import render_template, abort
from flask_login import login_required, current_user
from app.user import bp
from app.models import User
from flask import redirect, url_for


@bp.route("/")
@login_required
def me():
    return render_template("user/self.html", user=current_user)


@bp.route("/<username>/profile")
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template("user/profile.html", user=user)


@bp.route("/<username>")
def profile_redirect(username):
    return redirect(url_for("user.profile", username=username))
