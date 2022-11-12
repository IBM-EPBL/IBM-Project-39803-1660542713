from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re 
app = Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServercertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=tcv10068;PWD=0rvaGK1vXCyVfytj;", "", "")

@app.route('/')
@app.route('/account', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        stmt = ibm_db.exec_immediate(conn,'SELECT * FROM NEWSDB WHERE email = % s AND password = % s', (email, password, ))
        account = ibm_db.fetch_both(stmt)
        if username==password:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('account.html', msg = msg)

@app.route('/signup', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'fname' in request.form and 'password' in request.form and 'email' in request.form and 'lname' in request.form :
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServercertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=tcv10068;PWD=0rvaGK1vXCyVfytj;", "", "")
        stmt = ibm_db.exec_immediate(conn,'SELECT * FROM NEWSDB')
        if email==password:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', fname):
            msg = 'Username must contain only characters and numbers !'
        elif not fname or not password or not email:
            msg = 'Please fill out the form !'
        else:
            sql=ibm_db.exec_immediate(conn,'INSERT INTO NEWSDB (fname, lname, email, password) VALUES (%s, %s, %s, %s)')
            msg = 'You have successfully registered !'
            print("you have successfully registered!")
            return redirect(url('/signup'))
    elif request.method == 'POST':
            msg = 'Please fill out the form !'
    return render_template('account.html', msg = msg)

if __name__=='__main__':
    app.run(debug=True)
