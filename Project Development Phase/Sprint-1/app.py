from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re 
app = Flask(__name__)
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServercertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=mgb08180;PWD=mo1BSIxDPwEiXZ6a;", "", "")
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/register', methods =['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST'and 'fname' in request.form and 'lname' in request.form and 'email' in request.form and 'password' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        #cpassword = request.form['cpassword']
        stmt = ibm_db.prepare(conn,'SELECT * FROM REGISTER')
        ibm_db.blind_param(stmt, 1, fname)
        ibm_db.blind_param(stmt, 2, lname)
        ibm_db.blind_param(stmt, 3, email)
        ibm_db.blind_param(stmt, 4, password)
       # ibm_db.blind_param(stmt, 5, cpassword)
        ibm_db.execute(sql)
        account = ibm_db.fetch_assoc(stmt)
        if stmt:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
            
        else:
            sql=ibm_db.prepare(conn,'INSERT INTO REGISTER (roll_no, username, email, password, cpassword) VALUES (?, ?, ?, ?)')
            ibm_db.blind_param(sql, 1, fname)
            ibm_db.blind_param(sql, 2, lname)
            ibm_db.blind_param(sql, 3, email)
            ibm_db.blind_param(sql, 4, password)
            #ibm_db.blind_param(sql, 5, cpassword)
            ibm_db.execute(sql)
            msg = 'You have successfully registered !'
            return redirect(url('/login'))
    elif request.method == 'POST':
            msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        username = request.form['email']
        password = request.form['password']
        stmt = ibm_db.prepare(conn,'SELECT * FROM REGISTER WHERE email = % s AND password = % s', (email, password, ))
        ibm_db.blind_param(stmt,1,email)
        ibm_db.blind_param(stmt,2,password)
        ibm_db.exec(stmt)
        account = ibm_db.fetch_both(stmt)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('account.html', msg = msg)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/error')
def error():
    return render_template("404.html")
@app.route('/author')
def author():
    return render_template("author.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/post-category-1')
def post_category_1():
    return render_template("post-category-1.html")
@app.route('/post-category-2')
def post_category_2():
    return render_template("post-category-2.html")
@app.route('/post-full-width')
def post_full_width():
    return render_template("post-full-width.html")
@app.route('/post-left-sidebar')
def post_left_sidbar():
    return render_template("post-left-sidebar.html")
@app.route('/privacy')
def privacy():
    return render_template("privacy.html")
@app.route('/single-post')
def single_post():
    return render_template("single-post.html")
@app.route('/terms')
def terms():
    return render_template("terms.html")
if __name__ == "__main__":
    app.run(debug = True)