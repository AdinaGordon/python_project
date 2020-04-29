import flask
from flask import request
from request_data import RequestData
from request_data import create_request_data
from request_store_db import RequestStoreDb
from flask import json
from flask import Response
import traceback

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/AddMessage', methods=['POST'])
def add_message():
    try:
        r=create_request_data(request.json)
        if r.is_valid_post():
            store=RequestStoreDb()
            store.save_request(r)
            resp=Response(status=200, mimetype='application/json')
        else:
            resp=Response(status=400, mimetype='application/json')    
    except:
        traceback.print_exc()
        resp=Response(status=500, mimetype='application/json')    
    return resp

@app.route('/GetMessage', methods=['GET'])
def get_message():
    try:
        if is_valid_url_with_params(request.args):
            store=RequestStoreDb()
            filtered=store.get_requests(request)
            js=json.dumps(filtered,default=lambda x:x.__dict__)
            resp=Response(js, status=200, mimetype='application/json')
        else:
            resp=Response( status=400, mimetype='application/json')
    except:
        traceback.print_exc()
        resp=Response( status=500, mimetype='application/json')
    return resp

@app.route('/DeleteMessage', methods=['DELETE'])
def delete_message():
    try:
        if is_valid_url_with_params(request.args):
            store=RequestStoreDb()
            if store.delete_requests(request):
                resp=Response(status=200, mimetype='application/json')
            else:
                resp=Response(status=404, mimetype='application/json')
        else:
            resp=Response(status=400, mimetype='application/json')
    except:
            traceback.print_exc()
            resp=Response( status=500, mimetype='application/json')
    return resp

def is_valid_url_with_params(args):
    a = ('application_id' in args and args['application_id'] and str(args['application_id']).isnumeric() ) or 'session_id' in args and args['session_id'] or 'message_id' in args and args['message_id'] 
    return a 

if __name__ == "__main__":
    app.run()




