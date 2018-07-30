# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for,session
from models import Novels,Contents
import config
from exts import db
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
        content=Contents.query.filter(Contents.id==1).first()
        contents=content.content
        contents2=contents.split()

        return render_template('index.html',content=content,contents2=contents2)
@app.route('/detail/<id>')
def detail(id):
        content=Contents.query.filter(Contents.id==id).first()
        contents=content.content
        contents2=contents.split()

        return render_template('index.html',content=content,contents2=contents2)

if __name__ == '__main__':
    app.run()
