from flask import (Blueprint, render_template, request,
                   current_app, flash, session, redirect, url_for)
from database.sql_provider import SQLProvider
from database.operations import select_from_db, insert_into_db
from database.connection import DBContextManager

from decorators.routes import login_required, role_required

from datetime import date

basket_app = Blueprint('basket_app', __name__, template_folder='templates')
sql_provider = SQLProvider('basket/sql')


@basket_app.route('/', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def basket_index():
    if not session.get('basket'):
        session['basket'] = []

    sql_statement = sql_provider.get('select_all_details.sql', {})
    result = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)

    if request.method == 'POST':
        detail_id = request.form['code']
        price = request.form['price']
        quantity = int(request.form['quantity'])

        for item in session['basket']:
            if item['code'] == detail_id and item['price'] == price:
                item['quantity'] += quantity
                flash('Добавлено в накладную', 'okay')
                break
        else:
            session['basket'].append(
                {'code': request.form['code'],
                    'name': request.form['name'],
                    'material': request.form['material'],
                    'weight': request.form['weight'],
                    'price': price,
                    'quantity': quantity})
            flash('Добавлено в накладную', 'okay')
        session.modified = True

    return render_template('basket_index.html',
                           count=len(session['basket']),
                           result=result)


@basket_app.route('/show', methods=['GET'])
@login_required(session)
@role_required(session)
def show_basket_handler():
    basket = session.get('basket')
    if len(basket) == 0:
        flash('Накладная пуста', 'error')
        return redirect(url_for('basket_app.basket_index'))
    else:
        cost = 0
        for item in basket:
            cost += float(item['price']) * int(item['quantity'])
        return render_template('show_basket.html', basket=basket, cost=cost)


@basket_app.route('/delete-all', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def delete_all_handler():
    session['basket'] = []
    session.modified = True
    flash('Накладная очищена', 'okay')
    return redirect(url_for('basket_app.basket_index'))


@basket_app.route('/delete-current', methods=['POST'])
@login_required(session)
@role_required(session)
def delete_current_handler():
    basket = session.get('basket', [])
    session['basket'] = [product for product in basket if product['code']
                         != request.form.get('code')]
    session.modified = True

    return redirect(url_for('basket_app.show_basket_handler'))


@basket_app.route('/create-order', methods=['POST'])
@login_required(session)
@role_required(session)
def create_order_handler():
    username = session.get('user')
    basket = session.get('basket', [])
    date_now = date.today()

    sql_statement = sql_provider.get('select_sh_id.sql', {
        'username': username})
    sh_id = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)[0]['sh_id']

    sql_statement = sql_provider.get('create_invoice.sql', {
        'sh_id': sh_id,
        'date': date_now})
    insert_into_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)

    sql_statement = sql_provider.get('select_in_id.sql', {})
    in_id = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)[0]['in_id']

    with DBContextManager(current_app.config['MYSQL_DB_CONFIG']) as db:
        for item in basket:
            sql_statement = sql_provider.get('create_order.sql', {
                'quantity': int(item['quantity']),
                'price': item['price'],
                'in_id': in_id,
                'code': item['code']
            })
            db.execute(sql_statement)

    session['basket'] = []
    session.modified = True
    flash('Накладная успешно создана', 'okay')
    return redirect(url_for('basket_app.basket_index'))


@basket_app.route('/check-invoices', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def check_invoices():
    sql_statement = sql_provider.get('select_invoices.sql', {})
    result = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)

    if request.method == 'POST':
        code = request.form['code']
        sql_statement = sql_provider.get('update_invoices.sql', {'code': code})
        insert_into_db(current_app.config['MYSQL_DB_CONFIG'], sql_statement)
        flash('Статус накладной изменен', 'okay')
        return redirect(url_for('basket_app.check_invoices'))

    return render_template('invoices.html', result=result)
