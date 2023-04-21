
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

from ..app.database import db
from ..models import DataPull

data = Blueprint('data', __name__, url_prefix='/data')


@data.route('/pull')
def data_pull():
    data_pull: DataPull = DataPull.query.filter_by(hshd_num=10).all()
    return render_template('data_table.html', data_pull=data_pull)