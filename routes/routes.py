from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for, abort
from sqlalchemy import desc
from models.models import FightsDB

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def home_view():
    return redirect(url_for('home.competition_start'))


@home.route('/competition/<int:competition_id>')
def competition_view(competition_id):
    competition_id = competition_id
    # round_number = fight_create_func(round_number_prev)
    last_created_fight = FightsDB.query.filter_by(competition_id=competition_id).order_by(desc(FightsDB.fight_id)).first()

    return render_template("competition.html", fight_data=last_created_fight)
