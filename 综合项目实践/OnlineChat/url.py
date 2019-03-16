# coding=utf-8

"""
the url structure of website
"""

# import sys  # utf-8 兼容汉字
# reload(sys)
# sys.setdefaultencoding("utf-8")

from handlers.mainHandler import IndexHandler 
from handlers.mainHandler import ChatSocketHandler
from handlers.loginHandler import LogInHandler

url = [
    (r'/', IndexHandler),
    (r'/login.html', LogInHandler),
    (r'websocket', ChatSocketHandler),
]