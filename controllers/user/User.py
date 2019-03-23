# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify,make_response,g,redirect,render_template,current_app
from flask import session
from common.models.User import ( User )
from app import app,db
import json


route_user = Blueprint( 'user_page',__name__  )


@route_user.route( "/login",methods = [ "GET","POST" ] )
def login():
    if request.method == 'POST':
        current_app.logger.debug("login post method")
        username = request.form['username']
        password = request.form['password']

        user_info = User.query.filter_by( tea_email = username ).first()
        if not user_info:
            return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})

        if user_info.password != password:
            return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})
        session['username'] = username
        session['password'] = password
        session['tea_id'] = user_info.tea_id
        # response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
        # response.set_cookie('username', username)
        resp = make_response(render_template('index.html', name=user_info.tea_name))
        return resp
        #
        # if username == '123@123' and password == '123':
        #     session['username'] = username
        #     session['password'] = password
        #     current_app.logger.debug('in login %s %s'%(session.keys(),session.values()))
        #     resp = make_response(render_template('index.html', name=username))
        #     resp.set_cookie('username', username)
        #     current_app.logger.debug("cookie name %s" % request.cookies.get('username'))
        #     return resp
        #     #return jsonify({'status': '0', 'errmsg': '登录成功！'})
        # else:
        #     # return redirect(url_for('error'))
        #     return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})

    current_app.logger.debug("login get method")
    return render_template('auth-login.html')



@route_user.route( "/usr/loginin",methods = [ "GET","POST" ] )
def getinfo():
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    print("login_name:",login_name,"password:",login_pwd)
    user_info = User.query.filter_by(usrname=login_name)
    # if not user_info:
    #     return ("请输入正确的登录用户名和密码-1~~")
    # if user_info.password != login_pwd:
    #     return ("请输入正确的登录用户名和密码-1~~")

    return jsonify({'status': '0', 'errmsg': '登录成功！'})

