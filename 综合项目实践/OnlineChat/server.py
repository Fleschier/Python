# coding = utf-8


import tornado.ioloop
# mport tornado.options
from tornado.options import define, options
import tornado.web
import tornado.escape
import os.path
from handlers.mainHandler import IndexHandler 
from handlers.mainHandler import ChatSocketHandler
from handlers.loginHandler import LogInHandler

import uuid
import base64
secret_code = base64.b64encode(uuid.uuid4().bytes)      #使用cookie加密方法

def application():
    url = [
            (r'/', IndexHandler),
            (r'/login.html', LogInHandler),
            (r'/chat.html', ChatSocketHandler),
    ]
    settings = dict(
            cookie_secret=secret_code,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
    )
    return tornado.web.Application(handlers=url, **settings)

define("port", default = 8888, help = "run on the given port", type=int)

def main():
    tornado.options.parse_command_line()
    app = application()
    app.listen(options.port)

    # http_server = tornado.httpserver.HTTPServer(application)
    # http_server.listen(options.port)

    print("Development server is running at http://127.0.0.1:%s" % options.port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()
    # tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()

