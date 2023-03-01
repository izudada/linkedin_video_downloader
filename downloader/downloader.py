from flask import (
    Blueprint, flash, redirect, render_template, request, send_file, url_for
)
from werkzeug.exceptions import abort
from .linkedin_downloader import lk_downloader


bp = Blueprint('downloader', __name__)


@bp.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        linkedin_post = request.form['url']
        message = lk_downloader(linkedin_post)
        flash(message, 'danger')
        return redirect(url_for('index'))
    else:
        return render_template('index.html')
