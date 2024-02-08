from flask import (Blueprint, render_template, request,
                   session, current_app, redirect, flash, url_for)
from database.sql_provider import SQLProvider
from database.operations import select_from_db, insert_into_db

from datetime import datetime
from decorators.routes import login_required, role_required


access_app = Blueprint('access_app', __name__, template_folder='templates')
sql_provider = SQLProvider('access/sql')


@access_app.route('/', methods=['GET'])
def access_index():
    return render_template('access_index.html')


def user_exists(username):
    sql_statement = sql_provider.get(
        'check_user_doesnt_exist.sql', {'username': username})
    result = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)
    return bool(result)


@access_app.route('/login', methods=['POST'])
def login_handler():
    name, password = request.form['username'], request.form['password']
    data = {'user': name, 'password': password}

    if not user_exists(name):
        flash('Неправильный логин или пароль', 'error')
        return render_template('access_index.html')

    sql_statement = sql_provider.get(
        'check_role.sql',
        {'login': data['user'], 'password': data['password']})
    connect = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)

    if connect:
        session['user'] = name
        session['password'] = password
        session['is_auth'] = True
        session['role'] = connect[0]['role']
    else:
        flash('Неправильный логин или пароль', 'error')
        return render_template('access_index.html')
    return redirect('/')


@access_app.route('/register', methods=['GET', 'POST'])
def register_handler():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_exists(username):
            flash('Пользователь уже существует', 'error')
            return render_template('register.html')

        sql_statement = sql_provider.get(
            'add_user.sql', {'username': username, 'password': password})
        insert_into_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)
        flash('Пользователь успешно добавлен', 'okay')
        return redirect(url_for('access_app.access_index'))


@login_required(session)
@access_app.route('/logout', methods=['GET'])
def logout_handler():
    session.clear()
    return redirect('/')


@login_required(session)
@role_required(session)
@access_app.route('/account', methods=['GET', 'POST'])
def personal_account():
    if request.method == 'GET':
        sql_statement = sql_provider.get(
            'get_user_info.sql', {'username': session['user']})
        result = select_from_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        user_info = {'username': session['user']}

        if result:
            user_info['name'] = result[0]['name']
            user_info['city'] = result[0]['city']
            user_info['sh_date'] = result[0]['sh_date']
            user_info['sh_phone'] = result[0]['sh_phone']
        return render_template('account.html', user_info=user_info)

    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        phone_number = request.form.get('phone')
        date_now = datetime.now().strftime('%Y-%m-%d')

        sql_statement = sql_provider.get('add_info_about_user.sql',
                                         {
                                             'username': session['user'],
                                             'name': name,
                                             'city': city,
                                             'sh_date': date_now,
                                             'sh_phone': phone_number
                                         }
                                         )
        insert_into_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)
        flash('Информация успешно добавлена', 'okay')
        return redirect(url_for('access_app.personal_account'))
