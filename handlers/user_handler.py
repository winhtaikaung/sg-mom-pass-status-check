
import os
import tornado.web
import requests
from tornado import gen
from handlers.base_handler import BaseHandler
from middleware.passport_validator import base_passport_validator
from scraper.mom_scraper import MOMScrapper


class UserHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @base_passport_validator
    @gen.engine
    def get(self, params):
        mom_scrapper = MOMScrapper
        mom_param = {'travelDocNo': 'MA889475'}
        mom_request= requests.post(os.environ["MOM_URL"], mom_param)
        response = yield gen.Task(mom_scrapper.get_scrapped_result, self,mom_request.content)
        # mom_scrapper.get_scrapped_result(self, os.environ["AVAILABLE_RESPONSE"])
        self.respond(response, {}, 200)
