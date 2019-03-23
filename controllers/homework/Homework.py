# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify,make_response,g,redirect,render_template,current_app
from flask import session
from common.models.User import ( User )
from common.models.Course import ( Course )
from common.models.Student import ( Student )
from common.models.Homework import ( Homework )
from common.models.Problem import (Problem)
from app import app,db,db_sql
import json


route_homework = Blueprint( 'homework_page',__name__  )
cursor = db_sql.cursor()

@route_homework.route( "/homework/<homework_id>",methods = [ "GET","POST" ] )
def ShowHomework(homework_id):
    homework_info = Homework.query.filter_by(homework_id=homework_id).first()
    problem_info = Problem.query.filter_by(pcourse_id=homework_info.pcourse_id).all()
    print(homework_info,problem_info)
    return render_template("correction.html",homework_info=homework_info,problem_info=problem_info)


@route_homework.route( "/homework/Comment/<homework_id>",methods = [ "GET","POST" ] )
def SubmitComment(homework_id):
    homework_info = Homework.query.filter_by(homework_id=homework_id).first()
    homework_info.done = 2
    homework_info.comment = request.form['comment']

    return render_template("index.html")

@route_homework.route( "/homework/ckeck/<tea_id>",methods = [ "GET","POST" ] )
def Ckeck(tea_id):
    tea_id = session['tea_id']
    exe = "select class_id,scourse_id from class_info where tea_id = " + "tea_id"
    cursor.execute(exe)
    print(exe)
    class_setcourse_data = cursor.fetchall()
    print(class_setcourse_data)
    class_setcourse_title_data = []
    for p in class_setcourse_data:
        p = list(p)
        scourse_info = Course.query.filter_by( scourse_id = p[1] ).first()
        temp = scourse_info.scourse_title
        exe = "select count(*) from inclass where class_id = \"%s\" "%p[0]
        cursor.execute(exe)
        sum = cursor.fetchone()
        sum = sum[0]
        p.append(temp)
        p.append(sum)
        class_setcourse_title_data.append(p)
    print(class_setcourse_title_data)
    resp = make_response(render_template('index.html', class_setcourse_title = class_setcourse_title_data))
    return resp






