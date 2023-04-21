from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from ..app.database import db
from ..constants import ALLOWED_EXTENSIONS, UPLOAD_DIRECTORY
from ..utils import parse_uploaded_files

upload = Blueprint('upload', __name__)


@upload.route('/upload')
def upload_page():
    upload_success = request.args.get('uploadSuccess')
    return render_template('upload.html', upload_success=upload_success)


@upload.route('/uploader', methods=['GET','POST'])
def upload_data():
    if request.method == 'POST':
        
        if not request.files:    
            return redirect(url_for('upload.upload_page'))

        for _,file in request.files.items():
            if file.filename.endswith(ALLOWED_EXTENSIONS) and file.filename:
                file.save(f'{UPLOAD_DIRECTORY.resolve()}/{file.filename}')

        parse_uploaded_files()

        return redirect(f"{url_for('upload.upload_page')}?uploadSuccess=True")

    return redirect(url_for('upload.upload_page'))
