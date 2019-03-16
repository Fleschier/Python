#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-01-24 12:57:09
# @Author  : Linsir (vi5i0n@hotmail.com)
# @Link    : http://Linsir.sinaapp.com


import os
import sys
import tornado.ioloop
import tornado.web
import tornado.websocket
import json

clients = set()

def updatelist():
    total = len(clients)
    userlist = []
    for c in clients:
        userlist.append(c.username)
        # pass
    msg = {
    'type': 'list',
    'total': total,
    'userlist': userlist,
    }
    return msg

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")

class DemoHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("demo.html")

class ChatHandler(tornado.websocket.WebSocketHandler):
    username = "user"
    uid = "0"
    def check_origin(self, origin):
        return True

    def reg(self, uid, username):
        self.username = username
        self.uid = uid
        if self not in clients:
            clients.add(self)
        self.send_to_all({
            'type': 'sys',
            'username': 'SYSTEM',
            'uid': '1000',
            'message': username + '(' + uid + ') has joined!',
            })
        self.send_to_all(updatelist())

    def send_to_all(self, message):
        for c in clients:
            #print(c,"========================================")
            c.write_message(json.dumps(message))

    def open(self):
        self.write_message(json.dumps({
            'type': 'sys',
            'username': 'SYSTEM',
            'uid': '1000',
            'message': 'Welcome to Chat Room!',
            }))

    def on_close(self):
        clients.remove(self)
        self.send_to_all({
            'type': 'sys',
            'username': 'SYSTEM',
            'uid': '1000',
            'message': self.username + '(' + self.uid + ') has left!'
            })
        self.send_to_all(updatelist())

    def on_message(self, message):
        msg = json.loads(message)
        if msg["type"] == "reg":
            self.reg(msg["uid"], msg["username"])
        elif msg["type"] == "msg":
            if self not in clients:
                clients.add(self)
                try:
                    self.reg(msg["uid"], msg["username"])
                except Exception, e:
                    self.reg(self.uid, msg["username"])
            for c in clients:
                c.write_message(message)
        else:
            print "Message Error."
        

settings = {
    'debug': True,
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'gzip': True,
}

handlers = [
    (r'/', IndexHandler),
    (r'/demo',DemoHandler),
    (r'/chat',ChatHandler),
]

application = tornado.web.Application(handlers, **settings)

if __name__ == '__main__':
    application.listen(8003)
    tornado.ioloop.IOLoop.instance().start()