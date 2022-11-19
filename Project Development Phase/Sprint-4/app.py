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
    msg =''
    if request.method == 'POST':

        #try:

            roll_no = request.form['roll_no']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            sql = "SELECT * FROM register WHERE email = ?"
            stmt = ibm_db.prepare(conn, sql)
            ibm_db.bind_param(stmt, 1, email)
            ibm_db.execute(stmt)
            account = ibm_db.fetch_assoc(stmt)

            if account:
                msg = "Record Aldready found", "success"
            else:
                insert_sql = "insert into register(roll_no,username,email,password)values(?,?,?,?)"
                prep_stmt = ibm_db.prepare(conn, insert_sql)
                ibm_db.bind_param(prep_stmt, 1, roll_no)
                ibm_db.bind_param(prep_stmt, 2, username)
                ibm_db.bind_param(prep_stmt, 3, email)
                ibm_db.bind_param(prep_stmt, 4, password)
                ibm_db.execute(prep_stmt)
                msg = "Your Information Stored Successful."
                sql = "SELECT id FROM register WHERE email=?"
                stmt = ibm_db.prepare(conn, sql)
                ibm_db.bind_param(stmt, 1, email)
                ibm_db.execute(stmt)
        #except:
          #  msg = "Error in Insertion Operation"
       #finally:
            return redirect(url_for("login"))
         #   con.close()

    return render_template('signup.html', msg=msg)
"""def register():
    msg = ''
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServercertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=mgb08180;PWD=mo1BSIxDPwEiXZ6a;", "", "")
    if request.method == 'POST':

        try:


            roll_no= request.form['roll_no']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            stmt = ibm_db.prepare(conn,"SELECT * FROM register WHERE email = ?")
            ibm_db.bind_param(stmt, 1, email)
            ibm_db.execute(stmt)
            account = ibm_db.fetch_assoc(stmt)

            if account:
                msg = 'Account already exists'
            else:
                    prep_stmt = ibm_db.prepare(conn,'insert into register (roll_no, username, email, password) values (?, ?, ?, ?)')
                    ibm_db.bind_param(prep_stmt, 1, fname)
                    ibm_db.bind_param(prep_stmt, 2, lname)    
                    ibm_db.bind_param(prep_stmt, 3, email)
                    ibm_db.bind_param(prep_stmt, 4, password)    
                    ibm_db.execute(prep_stmt)
                    msg = 'You have successfully registered !'
                    sql = "SELECT id FROM REGISTER WHERE email=?"
                    stmt = ibm_db.prepare(conn, sql)
                    ibm_db.bind_param(stmt, 1, email)
                    ibm_db.execute(stmt)
                    ibm_db.fetch_tuples(stmt)
                    return redirect(url_for('/login'))
                else if: 
                        request.method == 'POST'
                        msg = "Please fill out the form !"
   # 0finally:
        return render_template('signup.html', msg = msg)"""
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        username = request.form['email']
        password = request.form['password']
        stmt = ibm_db.prepare(conn,'SELECT * FROM REGISTER WHERE email = % s AND password = % s', (email, password, ))
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
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
@app.route('/logged')
def logged():
    return render_template("logged.html")
if __name__ == "__main__":
    app.run(debug = True)