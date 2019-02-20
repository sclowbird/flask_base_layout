from flask import Blueprint, redirect, url_for, render_template

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/'
)


@main_blueprint.route('/')
def index():
    return render_template('base.html')


    