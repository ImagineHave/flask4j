from flask import Blueprint

bp = Blueprint('feeder', __name__, url_prefix='/feeder')

# a simple page that says hello
@bp.route('/hello')
def hello():
    return 'Hello, World!'