import sys
import flask
from flask import request
class RequestData:
    def __init__(self,application_id,session_id,message_id,participants,content):
        self.application_id=application_id
        self.session_id=session_id
        self.message_id=message_id
        self.participants=participants
        self.content=content
    
    def is_valid_post(self):
       return (self.application_id and isinstance(self.application_id, int)) and self.session_id and  self.message_id  
    
    def get_participants_as_string(self):
        str1=''
        if self.participants: 
            for p in self.participants:
                str1=str1+p+','
            if len(str1) > 0:
                str1=str1[:-1]
        return str1

def create_request_data(json):
    return RequestData(json.get('application_id'),json.get('session_id'),json.get('message_id'),json.get('participants'),json.get('content'))


    