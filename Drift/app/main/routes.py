from flask import render_template
from datetime import datetime
from app.main import bp


@bp.route("/")
def index():
    return render_template("index.html")


@bp.app_context_processor
def inject_now():
    return {"now": lambda: datetime.now()}
