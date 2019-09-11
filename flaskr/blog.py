from flask import (
    Blueprint,
    g,
    redirect,
    render_template,
    request,
    url_for,
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        author_id = g.user['id']
        db = get_db()

        db.execute(
            'INSERT INTO post (title, body, author_id)'
            ' VALUES (?, ?, ?)', (title, body, author_id)
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('blog/create.html')
