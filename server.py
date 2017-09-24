import os

from tornado.ioloop import IOLoop
import tornado.web

from handlers.base_handler import BaseHandler
from routes.messenger_route import messenger_routes
from routes.user_route import user_routes


class MainHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        # TODO generate Dummy data will be removed on production
        # self.'Hi I Am Windy Tornado\n Avaliable Routes \n\
        #            http:localhost:3000/api/v1/users')
        self.respond("Invalid Request", 404)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler)
        ]

        settings = {
            'debug': True
        }
        # This Method is to add all the routes from Route Package
        handlers.extend(user_routes)
        handlers.extend(messenger_routes)
        tornado.web.Application.__init__(self, handlers, settings)


def main():
    app = Application()
    app.listen(os.environ["PORT"])
    IOLoop.instance().start()


if __name__ == '__main__':
    main()

