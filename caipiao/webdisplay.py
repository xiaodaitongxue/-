from flask import Flask, render_template
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''连接数据库'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost:3306/caipiao?charset=utf8'.format('Huawei123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
DEBUG = True
db = SQLAlchemy(app)

class shuangseqiu(db.Model):
    riqi = db.Column(db.String(100), primary_key=True)
    red1 = db.Column(db.Integer)
    red2 = db.Column(db.Integer)
    red3 = db.Column(db.Integer)
    red4 = db.Column(db.Integer)
    red5 = db.Column(db.Integer)
    red6 = db.Column(db.Integer)
    blue = db.Column(db.Integer)


    def __init__(self, riqi, red1, red2, red3, red4, red5, red6, blue):
        self.riqi = riqi
        self.red1 = red1
        self.red2 = red2
        self.red3 = red3
        self.red4 = red4
        self.red5 = red5
        self.red6 = red6
        self.blue = blue



@app.route('/')
def show_all():
    return render_template('show_all.html', shuangseqiu=shuangseqiu.query.all())


app.run("127.0.0.1", 5001, debug=True)

with app.app_context():
    all_shuangseqiu = shuangseqiu.query.all()
