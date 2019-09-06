from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.security import generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()

        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, generate_password_hash(password))
        )
        db.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')
