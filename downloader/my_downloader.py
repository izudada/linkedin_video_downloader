from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from downloader.linkedin_downloader import lk_downloader


bp = Blueprint('downloader', __name__)

@bp.route('/', methods = ['GET', 'POST'])
def index():
    """
        An index function that accepts user input as a url
        to a linkedin post and streams a video related to the post
    """
    #   post request condition
    if request.method == 'POST':
        #   get user input 
        linkedin_post = request.form['url']
        #   call lk_downloader and pass in user input
        message = lk_downloader(linkedin_post)
        if message == "Downloded video sucessfully":
            flash(message, 'success')
        else:
            flash(message, 'danger')
        return redirect(url_for('index'))
    #   get request condition
    else:
        return render_template('index.html')
