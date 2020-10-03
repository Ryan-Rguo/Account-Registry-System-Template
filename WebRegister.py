# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import re
import sqlite3
import random
import hmac


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('registry_home.html')

@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')

@app.route('/signup', methods=['POST'])
def signup():
    try:
        # 4 elements in user database: usernames, salts, passwords, emails
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('select usernames from user')
        values = cursor.fetchall()
        names = []
        for v in values:
            names.append(v[0])
        print(names)

        cursor.execute('select emails from user')
        content = cursor.fetchall()
        emails = []
        for v in content:
            emails.append(v[0])
        print(emails)
    finally:
        cursor.close()
        conn.close()

    username = request.form['username']
    password = request.form['password']
    password2 = request.form['repeat_password']
    email = request.form['email']
    if re.match(r'^\w{6,}$', username) is None:
        return render_template('signup_form.html',
                               message='Username is a combination of at least 6 letters, numbers, or _')
    elif username in names:
        return render_template('signup_form.html', message='Username exists, please try another one!',
                               password=password, repeat_password=password2)

    if re.match(r'^\w{8,}$', password) is None:
        return render_template('signup_form.html',
                               message='Password is a combination of at least 8 letters, digits, or _',
                               username=username)
    elif password2 != password:
        return render_template('signup_form.html',
                               message='Repeated password is not correct!',
                               username=username)

    if email in emails:
        return render_template('signup_form.html',
                               message='Email exists, please try another one!',
                               username=username, password=password, repeat_password=password2)

    salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
    md5_psw = hmac.new(str.encode(password), str.encode(salt), digestmod='MD5').hexdigest()
    print(md5_psw)
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('insert into user (usernames, salts, passwords, emails) values (\'%s\', \'%s\', \'%s\', \'%s\')'
                       % (username, salt, md5_psw, email))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    return render_template('signup_ok.html', username=username)

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin_form.html')

@app.route('/signin', methods=['POST'])
def signin():
    input_user = request.form['username']
    input_psw = request.form['password']
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('select * from user where usernames=?', (input_user,))
        info = cursor.fetchall()
        if not info:
            return render_template('signin_form.html', message='Username does not exist!')
        if hmac.new(str.encode(input_psw), str.encode(info[0][1]), digestmod='MD5').hexdigest() != info[0][2]:
            return render_template('signin_form.html', message='Password is incorrect!', username=input_user)
    finally:
        cursor.close()
        conn.close()
    return render_template('signin_ok_registry.html', username=info[0][0], input_ps=input_user, salt=info[0][1],
                           md5=info[0][2], email=info[0][3])


if __name__ == '__main__':
    app.run()
# Open web browser, and input http://localhost:5000/ in address to start testing.
