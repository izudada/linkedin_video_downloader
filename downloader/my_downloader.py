from flask import (
    Blueprint, flash, jsonify, redirect, render_template, request, send_from_directory, session, url_for
)
from flask_cors import cross_origin
from downloader.linkedin_downloader import lk_downloader
import os


bp = Blueprint('downloader', __name__)

def get_server_path():
    """
        A function that gets the path of a server
        for locating a filename
    """
    if request.environ.get('HTTP_HOST') == '127.0.0.1:5000':
        path = os.path.expanduser("~")+"/Downloads/"
    else:
        path = os.path.expanduser("~")+"/"
    return path

@bp.route('/', methods = ['GET', 'POST'])
@cross_origin(origins="https://linkedinsave.xyz")
def index():
    """
        An index function that accepts user input as a url
        to a linkedin post and redirects to a success route
    """
    path = get_server_path()
    #   post request condition
    if request.method == 'POST':
        #   get user input 
        linkedin_post = request.form['url']
        #   call lk_downloader and pass in user input
        filename = lk_downloader(linkedin_post, path)
        return jsonify({'fileName': filename})
    #   get request condition
    else:
        return render_template('index.html')
    
@bp.route('/download/<filename>', methods = ['GET'])
@cross_origin(origins="http://127.0.0.1:5000, https://linkedinsave.xyz")
def download(filename):
    """
        An function that allows for video download
    """
    path = get_server_path()
    print(path, filename)
    try:
        return send_from_directory(path, filename, as_attachment=True), os.remove((path+filename))
    except Exception as e:
        print(e)
        flash("Video file not found. Please copy and paste the link again.", "danger")
        return redirect(url_for('index'))
