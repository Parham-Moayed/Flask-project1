from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Admin():
    def __init__(self,username,password):
        

        if(username and password=='admin'):
            @app.route('/admin')
            def show():
                
                @app.route('/admin-dash')
                def show1():
                    return redirect(url_for('admin-dash'))
                show1()
                return render_template('admin.html')
               
            show()
        if __name__ == '__main__':
            with app.app_context():
              db.create_all()
            app.run(debug=True)    
    