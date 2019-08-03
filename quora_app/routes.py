from flask import render_template, url_for, flash, redirect
from quora_app import app , db, bcrypt
from quora_app.forms import RegistrationForm, LoginForm
from flask_login import login_user

sql_insert_query = """INSERT INTO `user`
                      (`username`, `email`, `password`) VALUES (%s,%s,%s)"""

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        name = form.username.data
        emailId = form.email.data
        conn = db.connect()
        cursor =conn.cursor()
        cursor.execute(sql_insert_query,(name,emailId,hash_password))
        conn.commit()
        flash('Congratus Your Account Has Been Created! Enjoy:)','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

def checkDataBase(query):
    conn = db.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = (%s)",(query))
    data = cursor.fetchall()
    return data

def findDetails(emailId):
    return checkDataBase(emailId)



@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userData = findDetails(form.email.data)
        if userData:
            password = userData[0][3]
            if bcrypt.check_password_hash(password,form.password.data):
                login_user(userData[0][0],remember=form.remember.data)
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful! Password Incorrect','info')
        else:
            flash('Login Unsuccessful! Email Or Password Incorrect','info')
    return render_template('login.html',title='Login',form=form)
