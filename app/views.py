from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewsForm, FindEmail
from .models import Req

@app.route('/temp')
def temp():
    #news_list = News.query.order_by(News.created_date).all()
    #categories = Category.query.all()
    return render_template('template.html',
                           #news=news_list[::-1],
                           #categories=categories
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/notifications')
def notifications():
    return render_template('index.html')


@app.route('/hist', methods=['GET', 'POST'])
def hist():
    form = FindEmail()
    if form.validate_on_submit():
        mail = Req(form.email.data)
        #
        # надо сделать запрос в базу для поиска по имейлу
        #

        db.session.add(mail)
        db.session.commit()
        return redirect(url_for('history', id=mail.id))
    return render_template('history.html',
                           form=form)

@app.route('/history/<int:id>')
def history(id):
    form = FindEmail()
    if form.validate_on_submit():
        req = Req(email)
        #
        # надо сделать запрос в базу для поиска id for email
        #

        db.session.add(req)
        db.session.commit()
        return redirect(url_for('history', id=email.id))
    reqs = Req(id) # запрос в базу на получения списка запросов, поиск по имейлу
    return render_template('history.html',
                           form=form,
                           reqs=reqs)


@app.route('/category/<int:id>')
def news_in_category(id):
    return render_template('category.html')


@app.route('/add_req', methods=['GET', 'POST'])
def add_req():
    form = NewsForm()
    if form.validate_on_submit():

        req = Req()
        req.title = form.name.data
        req.text = form.email.data
        req.text = form.good.data
        req.text = form.discount.data

        mail = Req(form.email.data)
        #
        # надо сделать запрос в базу для поиска id for email
        #

        db.session.add(req)
        db.session.commit()
        return redirect(url_for('history', id=mail.id))
    return render_template('add_req.html',
                           form=form)