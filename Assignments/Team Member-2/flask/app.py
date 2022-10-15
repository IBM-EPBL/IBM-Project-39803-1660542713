from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re 
app = Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServercertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=thc92299;PWD=oZSXbt6fUbcbFOc1;", "", "")

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        username = request.form['email']
        password = request.form['password']
        stmt = ibm_db.exec_immediate(conn,'SELECT * FROM REGISTER WHERE email = % s AND password = % s', (email, password, ))
        account = ibm_db.fetch_both(stmt)
        if username==password:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'roll_no' in request.form :
        roll_no = request.form['roll_no']
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
        conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServercertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=mgb08180;PWD=Rw9HkOun2nVKLC5s;", "", "")
        stmt = ibm_db.exec_immediate(conn,'SELECT * FROM REGISTER')
        if email==cpassword:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            sql=ibm_db.exec_immediate(conn,'INSERT INTO REGISTER (roll_no, username, email, password, cpassword) VALUES (%s, % s, % s, % s)')
            msg = 'You have successfully registered !'
            print("you have successfully registered!")
            return redirect(url('/login'))
    elif request.method == 'POST':
            msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

if __name__=='__main__':
    app.run(debug=True)