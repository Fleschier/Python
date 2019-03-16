# #coding = utf-8
# # from url import url     #从url.py中引入网站目录结构

# # settings = dict(
# #     template_path = os.path.join(os.path.dirname(__file__), "templates"),
# #     static_path = os.path.join(os.path.dirname(__file__), "static"),        #注意这里static目录绝对不要加s!!
# #     debug = True        #服务器不重启就可以看到修改代码的效果
# # )

# # application = tornado.web.Application(
# #     handlers = url,
# #     **settings
# # )

# import tornado.web
# import os
# from handlers.mainHandler import IndexHandler 
# from handlers.mainHandler import ChatSocketHandler
# from handlers.loginHandler import LogInHandler

# import tornado.escape
# import os.path
# import uuid

# # url = [
# #     (r'/', IndexHandler),
# #     (r'/login.html', LogInHandler),
# #     (r'/chat.html', ChatSocketHandler),
# # ]



# class Application(tornado.web.Application):
#     def __init__(self):
#         handlers = [
#             (r'/', IndexHandler),
#             (r'/login.html', LogInHandler),
#             (r'/chat.html', ChatSocketHandler),
#         ],
#         settings = dict(
#             cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
#             template_path=os.path.join(os.path.dirname(__file__), "templates"),
#             static_path=os.path.join(os.path.dirname(__file__), "static"),
#             xsrf_cookies=True,
#         )

#         tornado.web.Application.__init__(self, handlers, **settings)

