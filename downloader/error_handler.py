from flask import Blueprint, Flask, render_template


bp = Blueprint('errors', __name__)


@bp.app_errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('error_templates/404.html'), 404

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('error_templates/500.html'), 500