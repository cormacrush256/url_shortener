from flask import Blueprint, redirect, request, render_template
from .models import URL_Connector
from .extensions import db

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = URL_Connector.query.filter_by(short_url=short_url).first_or_404()
    return redirect(link.original_url)

#home page
@short.route('/')
def index():
    return render_template('index.html')

#page that displays new shortened url
@short.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    url_connection = URL_Connector(original_url=original_url)
    db.session.add(url_connection)
    db.session.commit()
    return render_template('shortened_url.html',
                           new_link = url_connection.short_url, original_url=url_connection.original_url)

#error handling page for non-existent urls
@short.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404