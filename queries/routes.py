from typing import Tuple, Any
from flask import (
    Blueprint,
    render_template,
    request,
    current_app,
    flash,
    session
)

from database.sql_provider import SQLProvider
from database.operations import select_from_db, insert_into_db

from decorators.routes import login_required, role_required

queries_app: Blueprint = Blueprint(
    'queries_app', __name__, template_folder='templates')
sql_provider: SQLProvider = SQLProvider('queries/sql')


@queries_app.route('/')
@login_required(session)
@role_required(session)
def queries_index():
    """
    Обрабатывает главную страницу запросов.
    """
    return render_template('queries_index.html', role=session['role'])


def query_execution(key, sql_statement_name):
    """
    Выполняет SQL-запрос и возвращает результат.
    """
    data = request.form.get(key)

    if not data:
        return False, "Данные не введены"

    sql_statement = sql_provider.get(sql_statement_name, {key: data})
    result = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)

    if not result:
        return False, "Нет результатов"

    return True, result


@queries_app.route('/show-balance', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def show_balance():
    if request.method == 'GET':
        return render_template('show_balance.html')
    else:
        check_flag, result = query_execution(
            'name', 'show_balance.sql')

        if check_flag:
            return render_template('show_balance.html', result=result)
        else:
            flash(result, 'error')
            return render_template('show_balance.html', message=result)


@queries_app.route('/show-invoice-by-date', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def show_invoice_by_month():
    if request.method == 'GET':
        return render_template('show_invoice_by_month.html')
    else:
        check_flag, result = query_execution(
            'date', 'show_invoice_by_month.sql')

        if check_flag:
            return render_template('show_invoice_by_month.html', result=result)
        else:
            flash(result, 'error')
            return render_template('show_invoice_by_month.html', message=result)


@queries_app.route('/show-history', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def show_history_by_shipper():
    if request.method == 'GET':
        return render_template('show_history_by_shipper.html')
    else:
        check_flag, result = query_execution(
            'name', 'show_history_by_shipper.sql')

        if check_flag:
            return render_template('show_history_by_shipper.html', result=result)
        else:
            flash(result, 'error')
            return render_template('show_history_by_shipper.html', message=result)


@queries_app.route('/show-shippers', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def search_shippers_by_city():
    if request.method == 'GET':
        return render_template('search_shippers_by_city.html')
    else:
        check_flag, result = query_execution(
            'city', 'search_shippers_by_city.sql')

        if check_flag:
            return render_template('search_shippers_by_city.html', result=result)
        else:
            flash(result, 'error')
            return render_template('search_shippers_by_city.html', message=result)


@queries_app.route('/search-by-material', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def search_by_material_handler():
    if request.method == 'GET':
        return render_template('search_detail_by_material.html')
    else:
        check_flag, result = query_execution(
            'material', 'search_detail_by_material.sql')

        if check_flag:
            return render_template('search_detail_by_material.html', result=result)
        return render_template('search_detail_by_material.html', message=result)
