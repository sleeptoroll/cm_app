from . import api
from cm_app import db

@api.route("/index")
def index():
    return "index page"