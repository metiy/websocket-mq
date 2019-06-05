#!/usr/bin/python

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class PubHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        for client in clients.keys():
            client.write_message( message)

    def on_close(self):
        pass

    def check_origin(self, origin):
        return True

class SubHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        if ( message == 'sub') :
            clients[self] = 1
        elif (message == 'unsub') :
            del clients[self]

    def on_close(self):
        pass

    def check_origin(self, origin):
        return True

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/pub', PubHandler),
            (r'/sub', SubHandler)
        ]

        settings = {
            'template_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    clients = {}
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(4888)
    tornado.ioloop.IOLoop.instance().start()
