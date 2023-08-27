from . import main_blueprint
from flask import render_template, request, redirect, url_for
from app import db

@main_blueprint.get('/')
def root():
    db.create_all()
    return render_template('main/landing_page.html')

