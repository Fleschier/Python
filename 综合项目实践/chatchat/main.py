import tornado.ioloop
import tornado.web
import os
import time

session = {}
session["users"] = []
session["rooms"] = {
    "defalut": {
        "description": "系统自带聊天室",
        "creater": "default",
        "members": [],
        "messages": [{
            "content": "系统消息: 富强民主文明和谐 自由平等公正法制 爱国敬业诚信友善",
            "author": "default",
            "create_time": "2019-03-09 00:00:00"
        }],
    }
}

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        current_num = len(session["users"])
        user_names = session["users"]
        rooms = session["rooms"]

        self.render("index.html", name=name, current_num=current_num, user_names=user_names, rooms=rooms)



class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        user_name = self.get_argument("name")
        session["users"].append(user_name)
        self.set_secure_cookie("user", user_name)
        self.redirect("/")


class LogoutHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        else:
            self.redirect("/")
            return

    def post(self):

        user_name = tornado.escape.xhtml_escape(self.current_user)
        if user_name in session["users"]:
            session["users"].remove(user_name)
        self.clear_all_cookies()
        self.redirect("/")

class AddroomHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        else:
            self.redirect("/")
            return    

    def post(self):
        if not self.current_user:
            self.redirect("/login")
            return
        roomname = self.get_argument("roomname")
        description = self.get_argument("description")
        creater = tornado.escape.xhtml_escape(self.current_user)

        session["rooms"][roomname] ={
            "description": description,
            "creater": creater,
            "members": [],
            "messages": [],
        }
        print(session)
        self.redirect("/")
        return


class JoinroomHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        roomname = self.get_argument("roomname")
        current_user_name = tornado.escape.xhtml_escape(self.current_user)
        if current_user_name not in session["rooms"][roomname]["members"]:
            session["rooms"][roomname]["members"].append(current_user_name)
        print(session)
        self.redirect("/")
        return

class QuitroomHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        roomname = self.get_argument("roomname")
        current_user_name = tornado.escape.xhtml_escape(self.current_user)
        if current_user_name in session["rooms"][roomname]["members"]:
            session["rooms"][roomname]["members"].remove(current_user_name)
        print(session)
        self.redirect("/")
        return

class EnterroomHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return 
        roomname = self.get_argument("roomname")
        current_user_name = tornado.escape.xhtml_escape(self.current_user)
        if roomname not in session["rooms"] or current_user_name not in session["rooms"][roomname]["members"]:
            self.redirect("/")
            return

        name = tornado.escape.xhtml_escape(self.current_user)
        current_num = len(session["users"])
        user_names = session["users"]
        rooms = session["rooms"]
        current_room_name = self.get_argument("roomname")
        
        self.render("room.html", name=name, current_num=current_num, user_names=user_names, rooms=rooms, current_room_name=current_room_name)
        

class DeleteroomHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return 
        roomname = self.get_argument("roomname")
        current_user_name = tornado.escape.xhtml_escape(self.current_user)
        if current_user_name != session["rooms"][roomname]["creater"]:
            self.redirect("/")
            return

        session["rooms"].pop(roomname)
        self.redirect("/")


class Sendhandler(BaseHandler):
    def post(self):
        if not self.current_user:
            self.redirect("/login")
            return 
        current_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        message_content = self.get_argument("message_content")
        roomname = self.get_argument("roomname")
        current_user_name = tornado.escape.xhtml_escape(self.current_user)
        current_message = {
                "content": message_content,
                "author": current_user_name,
                "create_time": current_time,
        }
        session["rooms"][roomname]["messages"].append(current_message)
        self.redirect("/enterroom?roomname=" + roomname)
        return 


        
        



        
        



        


    

def make_app():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/logout", LogoutHandler),
        (r"/addroom", AddroomHandler),
        (r"/joinroom", JoinroomHandler),
        (r"/quitroom", QuitroomHandler),
        (r"/enterroom", EnterroomHandler),
        (r"/deleteroom", DeleteroomHandler),
        (r"/send", Sendhandler),
    ], cookie_secret="chatchat12345")

    return application

if __name__ == "__main__":
    app = make_app()
    print(app.settings)
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()