from flask import Blueprint

bp = Blueprint('reader', __name__, url_prefix='/reader')

# a simple page that says hello
@bp.route('/hello')
def hello():
    return 'Hello, World!'