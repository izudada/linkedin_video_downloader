from flask import (
    Blueprint, flash, jsonify, redirect, render_template, request, send_from_directory, session, url_for
)
from downloader.linkedin_downloader import lk_downloader
import os


bp = Blueprint('downloader', __name__)


@bp.route('/', methods = ['GET', 'POST'])
def index():
    """
        An index function that accepts user input as a url
        to a linkedin post and redirects to a success route
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
        session['path'] = path
        session['filename'] = filename
        return jsonify(
            {'fileName': filename,
             'path': path
            }
        )
    #   get request condition
    else:
        return render_template('index.html')
    
@bp.route('/download', methods = ['GET'])
def download():
    """
        An function that allows for video download
    """
    path = session['path']
    filename = session['filename']
    return send_from_directory(path, filename, as_attachment=True), os.remove((path+filename)), session.clear()
