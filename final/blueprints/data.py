
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from ..app.database import db
from ..models import DataPull

data = Blueprint('data', __name__, url_prefix='/data')


@data.route('/pull')
def data_pull():
    household_num = request.args.get('household_num')
    data_pull = None

    if household_num:
        data_pull: DataPull = DataPull.query.filter_by(hshd_num=household_num).all()
    return render_template('data_table.html', data_pull=data_pull, household_num=household_num)


@data.route('/sample')
def data_pull_sample():
    return redirect(f"{url_for('data.data_pull')}?household_num=10")