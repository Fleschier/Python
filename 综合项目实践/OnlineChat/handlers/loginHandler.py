#!/usr/bin/env Python
# coding=utf-8

import tornado.web

class LogInHandler(tornado.web.RequestHandler):
    def get(self):
        # username = self.get_argument("user")
        # user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        self.render("login.html")

    # 因为是用post方法传的数据(在html中form标签的method为post)，那么在这个类中就要有post方法来接收数据。所以，要在IndexHandler类中增加post()
    def post(self):
        username = self.get_argument("username")    #参数是从前端传到后端的那个json对象的键的名字，是哪个键就获取该键的值
        password = self.get_argument("password")
        self.write("Welcome! " + username)    #后端向前端返回数据,返回一个字符串