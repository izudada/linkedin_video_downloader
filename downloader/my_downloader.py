import os
import socket

from flask import (
    Blueprint, flash, jsonify, redirect, render_template, request, send_from_directory, session, url_for
)
from flask_cors import cross_origin

from downloader.linkedin_downloader import _lk_downloader


bp = Blueprint('downloader', __name__)


def _get_server_path():
    current_directory = os.getcwd()

    # Construct the path to the 'videos' directory
    path = os.path.join(current_directory, 'videos')
    return path



@bp.route('/', methods = ['GET', 'POST'])
@cross_origin(origins="https://linkedinsave.xyz")
def index():
    """
        An index function that accepts user input as a url
        to a linkedin post and redirects to a success route
    """
    path = _get_server_path()
    #   post request condition
    if request.method == 'POST' and request.headers.get('X-Requested-With'):
        #   get user input 
        linkedin_post = request.form['url']
        #   call lk_downloader and pass in user input
        filename = _lk_downloader(linkedin_post, path)
        return jsonify({'fileName': filename})
    #   get request condition
    else:
        return render_template('index.html')
    
@bp.route('/download/<filename>', methods = ['GET'])
@cross_origin(origins="https://linkedinsave.xyz")
def download(filename):
    """
        An function that allows for video download
    """
    path = _get_server_path()
    try:
        return send_from_directory(path, filename, as_attachment=True), os.remove((path+filename))
    except Exception as e:
        print(e)
        flash("Video file not found. Please copy and paste the link again.", "danger")
        return redirect(url_for('index'))
