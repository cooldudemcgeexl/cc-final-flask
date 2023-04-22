from flask import Blueprint, jsonify, request
from flask_login import login_required

from ..app.database import db
from ..models import DataPull, Household, Product, Transaction

hshd_num = 10
product_num = 7

test = Blueprint("test", __name__, url_prefix="/test")


@test.route("/household")
@login_required
def household_test():
    household_num = request.args.get("hshd_num")
    household: Household = Household.query.filter_by(hshd_num=household_num).first()
    return jsonify(household)


@test.route("/product")
@login_required
def product_test():
    product: Product = Product.query.filter_by(product_num=product_num).first()
    return jsonify(product)


@test.route("/datapull")
@login_required
def data_pull_test():
    data_pull: DataPull = DataPull.query.filter_by(hshd_num=10).all()
    return jsonify(data_pull)
