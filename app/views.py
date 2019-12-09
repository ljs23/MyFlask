from flask import Blueprint

bp = Blueprint('blue',__name__)

@bp.route('/hello/')
def hello_world():
    return 'Hello World'

a=100
print(a)

