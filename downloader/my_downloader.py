from flask import (
    Blueprint, flash, redirect, render_template, request, send_from_directory, url_for
)
from downloader.linkedin_downloader import lk_downloader
import os


bp = Blueprint('downloader', __name__)


@bp.route('/', methods = ['GET', 'POST'])
def index():
    """
        An index function that accepts user input as a url
        to a linkedin post and streams a video related to the post
    """

    #   post request condition
    if request.method == 'POST':
        if request.environ.get('HTTP_HOST') == '127.0.0.1:5000':
            path = os.path.expanduser("~")+"/Downloads/"
        else:
            path = os.path.expanduser("~")+"/"
        #   get user input 
        linkedin_post = request.form['url']
        #   call lk_downloader and pass in user input
        filename = lk_downloader(linkedin_post, path)
        try:
            return send_from_directory(path, filename, as_attachment=True), os.remove((path+filename))
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            flash('Error Downloading Video', 'danger')
            return redirect(url_for('index'))
    #   get request condition
    else:
        return render_template('index.html')
