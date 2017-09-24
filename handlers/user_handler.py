import uuid

import os
import tornado.web
from pip._vendor import requests
from tornado import gen
from handlers.base_handler import BaseHandler, NO_CONTENT_ERROR
from scraper.mom_scraper import MOMScrapper


class UserHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.engine
    def get(self, params):
        mom_scrapper = MOMScrapper
        mom_param = {'travelDocNo': 'MA889475'}
        r = requests.post(os.environ["MOM_URL"], params)
        yield gen.Task(mom_scrapper.get_scrapped_result, self,r.content)
        # mom_scrapper.get_scrapped_result(self, os.environ["AVAILABLE_RESPONSE"])
        self.respond({}, {}, 200)

    @tornado.web.asynchronous
    @gen.engine
    def post(self, action):
        # user_repo = user_repository.UserRepository()
        # user = User(id=str(uuid.uuid4().hex), name=self.get_body_argument("name"),
        #             email=self.get_body_argument("email"),
        #             profile=self.get_body_argument("profile"),
        #             nric_no=self.get_body_argument("nricno"),
        #             address=self.get_body_argument("address"),
        #             zipcode=self.get_body_argument("zipcode"),
        #             )

        # response = yield gen.Task(user_repo.create_user, user)
        response = {}
        self.respond(response, 200)
