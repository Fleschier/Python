#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import tornado.websocket
import logging


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=ChatSocketHandler.cache)

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200
 
    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True
 
    def open(self):
        print ("new client opened")
        ChatSocketHandler.waiters.add(self)
 
    def on_close(self):
        ChatSocketHandler.waiters.remove(self)
 
    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]
 
    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)
 
    def on_message(self, message):
        logging.info("got message %r", message)
 
        ChatSocketHandler.send_updates(message)