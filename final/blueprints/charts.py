import json

import pandas as pd
import plotly
import plotly.express as px
from flask import Blueprint, redirect, render_template, request, url_for

from ..app.database import db
from ..constants.postgres import POSTGRES_CON_STR
from ..models import DataPull

charts = Blueprint("charts", __name__)


@charts.route("/charts")
def make_charts():
    dp_string = db.session.query(DataPull).statement
    data_pull_df = pd.read_sql(dp_string, POSTGRES_CON_STR)
    by_hshd_num_df = data_pull_df.groupby(["hshd_num"]).agg(
        spend=("spend", "sum"),
        children=("children", lambda x: x.iloc[0]),
        hshd_size=("hshd_size", lambda x: x.iloc[0]),
        income_range=("income_range", lambda x: x.iloc[0]),
    )
    by_hshd_num_df = by_hshd_num_df.fillna(0)

    print(by_hshd_num_df)

    by_children_df = by_hshd_num_df.groupby(["children"])["spend"].mean()
    print(by_children_df)
    by_hshd_size = by_hshd_num_df.groupby(["hshd_size"])["spend"].mean()
    by_income = by_hshd_num_df.groupby(["income_range"])["spend"].mean()

    fig1 = px.bar(by_children_df, labels={"children": "Children", "value": "Spending"})
    fig2 = px.bar(
        by_hshd_size, labels={"value": "Spending", "hshd_size": "Household Size"}
    )
    fig3 = px.bar(
        by_income, labels={"value": "Spending", "income_range": "Income Range"}
    )

    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template(
        "charts.html",
        graph1JSON=graph1JSON,
        graph2JSON=graph2JSON,
        graph3JSON=graph3JSON,
    )
