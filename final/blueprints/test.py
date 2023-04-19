from flask import Blueprint, jsonify
from flask_login import login_required

from ..models import Household

hshd_num= 10

test = Blueprint('test', __name__, url_prefix='/test')

@test.route('/household')
def household_test():
    household: Household = Household.query.filter_by(hshd_num=hshd_num).first()
    return jsonify(household)

