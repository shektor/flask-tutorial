from flask import (
    Blueprint,
    render_template
)

bp = Blueprint('blog', __name__)


@bp.route('/create')
def create():
    return render_template('blog/create.html')
