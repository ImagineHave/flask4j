from flask import Blueprint, jsonify, request

bp = Blueprint('feeder', __name__, url_prefix='/feeder')

# a simple page that says feeder
@bp.route('/')
def hello():
    return 'feeder'
    
# a simple page that says feeder
@bp.route('/upload', methods=['POST'])
def upload():
    '''lets make a standard file to upload'''
    
    dataDict = request.get_json()
    
    print(dataDict)
    return ('', 204)
    
# a simple page that says feeder
@bp.route('/load', methods=['GET'])
def load():
    '''load the bible into the database'''
    return 'load'