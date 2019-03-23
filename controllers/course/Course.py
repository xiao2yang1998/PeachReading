# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify,make_response,g,redirect,render_template,current_app
from flask import session
from common.models.User import ( User )
from common.models.Course import ( Course )
from common.models.Student import ( Student )
from app import app,db,db_sql
import json


route_course = Blueprint( 'course_page',__name__  )
cursor = db_sql.cursor()

@route_course.route( "/course",methods = [ "GET","POST" ] )
def ShowCourses():
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
    resp = make_response(render_template('course.html', class_setcourse_title = class_setcourse_title_data))
    return resp


@route_course.route( "/course/<class_id>",methods = [ "GET","POST" ] )
def ShowClassInfo(class_id):
    exe = "select scourse_id from class_info where class_id = " + "class_id"
    cursor.execute(exe)
    scourse_id = cursor.fetchone()
    scourse_id = scourse_id[0]
    scourse_info = Course.query.filter_by(scourse_id = scourse_id).first()
    exe = '''select count(*) from s_p_class_info where scourse_id = \"%s\" '''%scourse_id
    cursor.execute(exe)
    pcourse_num_data = cursor.fetchone()
    # get the num of the course
    pcourse_num_data = pcourse_num_data[0]
    # get the student of the class
    exe = 'select stu_id from inclass where class_id = \"%s\"'%class_id
    cursor.execute(exe)
    stu_id_data = cursor.fetchall()
    stu_homework_data= {}
    print(stu_id_data)
    # get the homework of the student
    for stu_id in stu_id_data:
        exe = 'select homework_id,done,thenumber from homework_info natural join s_p_class_info where stu_id=\"%s\" and class_id = \"%s\" order by thenumber'%(stu_id[0],class_id)
        cursor.execute(exe)
        homework_data = cursor.fetchall()
        stu_homework_data[stu_id[0]] = homework_data
    resp = make_response(render_template('onecour.html',scourse_info = scourse_info,pcourse_num = pcourse_num_data,stu_homework = stu_homework_data))
    return resp







