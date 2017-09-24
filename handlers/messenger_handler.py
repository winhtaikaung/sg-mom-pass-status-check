#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os


import tornado
from tornado import gen

from handlers.base_handler import BaseHandler

class MessengerHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, params):
        if self.get_argument("hub.mode") == "subscribe" and self.get_argument("hub.challenge"):
            if not self.get_argument("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
                return self.send_error({}, 403)
            print ("BOT HANDSHAKE complete")
            return self.write(self.get_argument("hub.challenge"))

    @tornado.web.asynchronous
    @gen.engine
    def post(self, action):
        msg_body = json.loads(self.request.body)
        merchant_repo = merchant_repository.MerchantRepository()
        if msg_body["object"] == "page":
            for entry in msg_body["entry"]:
                if entry.get("messaging"):
                    for messaging_event in entry["messaging"]:
                        sender_id = messaging_event["sender"]["id"]
                        recipient_id = messaging_event["recipient"]["id"]
                        if messaging_event.get("message"):

                            if messaging_event["message"].get("text"):
                                message_text = messaging_event["message"]["text"]

                                if messaging_event["message"].get("quick_reply"):
                                    """
                                    HERE IS quick Reply Area
                                    """
                                    payload = messaging_event["message"]["quick_reply"]["payload"]

                                    if payload == "NEAR_BY_PAYLOAD":
                                        send_location_reply(sender_id, "Can you tell me where you are?")
                                    elif payload == "RECOMMEND_ME_PAYLOAD":
                                        response = {}
                                        #yield gen.Task(merchant_repo.get_random_merchants, 5)
                                        send_list_templates(sender_id, response)
                                    elif payload == "LOCATION_NEGATIVE_PAYLOAD":
                                        send_quick_reply(sender_id, "Okie Dokie\nLet me check something new ;)")
                                else:
                                    send_typing_on(recipient_id=sender_id)
                                    send_quick_reply(recipient_id=sender_id,
                                                     message="Hello!\nI am Owlie 🦉,your personal fun manager in town.\nHow may I help you to find fun things for you?")
                                    send_typing_off(recipient_id=sender_id)
                            elif messaging_event["message"].get("attachments"):
                                if messaging_event["message"]["attachments"][0]["payload"].get("coordinates"):
                                    lat = messaging_event["message"]["attachments"][0]["payload"]["coordinates"]["lat"]
                                    lon = messaging_event["message"]["attachments"][0]["payload"]["coordinates"]["long"]
                                    response = {}
                                    #yield gen.Task(merchant_repo.get_nearby_merchants, 10, lat, lon)
                                    send_list_templates(sender_id, response)

                        if messaging_event.get("delivery"):  # delivery confirmation
                            pass

                        if messaging_event.get("optin"):  # optin confirmation
                            pass

                        if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                            print (messaging_event)
                            if messaging_event["postback"]["payload"] == "NOT_THIS_ONE":
                                send_quick_reply(sender_id, "Okie ;) \nHang on ")
                            if messaging_event["postback"]["payload"] == "GET_STARTED_PAYLOAD":
                                send_quick_reply(sender_id,
                                                 "Have a good day to you! How may I help you to find something for you?")
                            pass
                elif entry.get("postback"):
                    print ("callback")
                    pass

        self.respond({}, 200)
