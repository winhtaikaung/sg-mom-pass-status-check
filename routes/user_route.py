from handlers.user_handler import UserHandler

user_routes = [
    # (r'/api/v1/user/(?P<param1>[^\/]+)/?(?P<param2>[^\/]+)?/?(?P<param3>[^\/]+)?', UserHandler),
    (r'/api/v1/user/?(.*)', UserHandler)
]
