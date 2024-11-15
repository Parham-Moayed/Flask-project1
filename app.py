from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
from admin import Admin
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('index.html',title='Parham Moayed',name='Parham Moayed',website='Parham Moayed')
@app.route('/user/<name>')
def user(name):
    return name

    
@app.route('/result', methods=['POST'])
def submit():
    username = request.form.get('name')
    email = request.form.get('email')
    comment=request.form.get('comment')
    new_user = User(username=username, email=email,comment=comment)
    db.session.add(new_user)
    db.session.commit()
    return render_template('result.html')
   
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    comment=db.Column(db.Text,nullable=False)
  #  score=db.Column(db.Integer)
@app.route('/users')
def show_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append(f"ID: {user.id}, username: {user.username}, email: {user.email},comment :{user.comment}")
    
    user_list_html = '<br>'.join(user_list)
    return f"""
    <h2>لیست کاربران:</h2>
    <ul>
    {user_list_html}
    </ul>
    <br>
    <a href="/">برو به خانه</a>
    <br>
    <br><br><br>
    <form action="/users" method="post">
        <input type="text" name="getid">
        <br><br>
        <button type="submit">تغییر</button>
    </form>
    """
@app.route('/users',methods=['POST'])
def delete_commnet():
     getid=request.form.get('getid')
     getid=int(getid)
     comment = User.query.get_or_404(getid)
     db.session.delete(comment)
     db.session.commit()
     return redirect(url_for('home'))
@app.route('/survey')
def showCom():
    users = User.query.all()
        

    return render_template('survey.html',users=users)
@app.route('/admin',methods=['GET','POST'])
def adm():
    username=request.form.get('username')
    password=request.form.get('password')
    Admin(username,password)
    return render_template('admin.html')    

    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)