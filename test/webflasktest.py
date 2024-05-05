from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''连接数据库'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Huawei123@localhost:3306/shop?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

DEBUG = True
db = SQLAlchemy(app)
# db.create_all()
class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

# db.create_all()
# db.session.add(students)
# db.create_all()

@app.route('/')
def show_all():
    return render_template('show_all.html', students=students.query.all())


app.run("127.0.0.1", 5000, debug=True)

with app.app_context():
    # all_students = students.query.filter_by(city = ’Hyderabad’).all()
    # db.create_all()
    # db.session.add(students)
    all_students = students.query.all()