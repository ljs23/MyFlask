from flask import Blueprint

bp = Blueprint('blue',__name__)

@bp.route('/hello/')
def hello_world():
    return 'Hello World'
a=10
print(a)
