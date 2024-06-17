from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with current_app.app_context():
            user = current_app.users.get(username)

        if user and user.password == password:
            login_user(user)  # 登录用户
            return redirect(url_for('plist_list'))
        else:
            return render_template('login.html', error=True)

    return render_template('login.html')


@auth.route('/logout')
@login_required  # 要求用户登录才能注销
def logout():
    logout_user()  # 注销用户
    return redirect(url_for('index'))
