# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify,make_response,g,redirect,render_template,current_app
from flask import session
from common.models.User import ( User )
from common.models.Course import ( Course )
from common.models.Student import ( Student )
from common.models.Problem import (Problem)
from app import app,db,db_sql
import json


route_student = Blueprint( 'student_page',__name__  )
cursor = db_sql.cursor()

@route_student.route( "/student",methods = [ "GET","POST" ] )
def ShowStudents():
    tea_id = session['tea_id']
    exe = '''
      select stu_id,class_id from inclass where class_id in 
     (select class_id from class_info where tea_id = \"%s\")''' % tea_id
    cursor.execute(exe)
    stu_class_data = cursor.fetchall()
    current_app.logger.debug(stu_class_data)
    resp = make_response(render_template('student.html', student_class=stu_class_data))
    return resp


@route_student.route( "/student/<stu_id>",methods = [ "GET","POST" ] )
def ShowStudentInfo(stu_id):
    stu_info = Student.query.filter_by(stu_id = stu_id).first()
    exe = 'select class_id from inclass where stu_id = \"%s\"' % stu_id
    cursor.execute(exe)
    all_class_id = cursor.fetchall()
    class_homework_data = {}
    for class_id in all_class_id:
        class_id = class_id[0]
        exe = "select scourse_id from class_info where class_id = " + "class_id"
        cursor.execute(exe)
        scourse_id = cursor.fetchone()
        scourse_id = scourse_id[0]
        exe = 'select scourse_id,homework_id,done,thenumber from homework_info natural join s_p_class_info where stu_id=\"%s\" and class_id = \"%s\" and scourse_id=\"%s\" order by thenumber' % (
        stu_info.stu_id, class_id,scourse_id)
        cursor.execute(exe)
        homework_data = cursor.fetchall()
        class_homework_data[class_id] = homework_data
        print(class_homework_data)
        for i in class_homework_data:
            print(class_homework_data[i][0][0])
    resp = make_response(render_template('onestu.html', student= stu_info,class_homework=class_homework_data))
    return resp




