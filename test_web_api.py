import requests
import json

def test_valid_post_response_OK():
    do_delete('?application_id=1')
    # Body
    payload={"application_id": 1,
    "session_id": "aaaa",
    "message_id": "bbbb",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp_post=do_post(payload)
    resp_get = do_get('?application_id=1')
    assert resp_post.status_code == 200
    assert len(resp_get.json())==1
    assert resp_get.json()[0]["application_id"]==1 
    assert resp_get.json()[0]["session_id"]=='aaaa'
    assert resp_get.json()[0]["message_id"]=='bbbb'
    assert len(resp_get.json()[0]["participants"] ) == 2
    assert resp_get.json()[0]["participants"][0]=='avi aviv'
    assert resp_get.json()[0]["participants"][1]=='moshe cohen'  
    assert resp_get.json()[0]["content"]=='Hi, how are you today?' 

def test_valid_post_no_partipants_response_OK():
    do_delete('?application_id=1')
    # Body
    payload={"application_id": 1,
    "session_id": "aaaa",
    "message_id": "bbbb",
    "content": "Hi, how are you today?"
    }
    resp_post=do_post(payload)
    resp_get = do_get('?application_id=1')
    assert resp_post.status_code == 200
    assert len(resp_get.json())==1
    assert resp_get.json()[0]["application_id"]==1 
    assert resp_get.json()[0]["session_id"]=='aaaa'
    assert resp_get.json()[0]["message_id"]=='bbbb'
    assert len(resp_get.json()[0]["participants"] ) == 0
    assert resp_get.json()[0]["content"]=='Hi, how are you today?' 
 
def test_missing_application_id_field_post_response_bad_request():
    # Body
    payload={
    "session_id": "aaaa",
    "message_id": "bbbb",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp=do_post(payload)
    assert resp.status_code == 400

def test_application_id_not_int_post_response_bad_request():
    payload={"application_id":'1',
    "session_id": "aaaa",
    "message_id": "bbbb",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp=do_post(payload)
    assert resp.status_code == 400
    
def test_missing_session_id_value_post_response_bad_request():
    # Body
    payload={"application_id":1,
    "session_id": "",
    "message_id": "bbbb",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp=do_post(payload)
    assert resp.status_code == 400

    


def test_missing_message_id_field_post_response_bad_request():
    payload={"application_id": 1,
    "session_id": "aaaa",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp=do_post(payload)
    assert resp.status_code == 400

def test_missing_message_id_value_post_response_bad_request():
    # Body
    payload={"application_id":1,
    "session_id": "aaaa",
    "message_id": "",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp=do_post(payload)
    assert resp.status_code == 400

def test_missing_session_id_field_post_response_bad_request():
    payload={
    
    "message_id": "bbbb",
    "participants": ["avi aviv", "moshe cohen"],
    "content": "Hi, how are you today?"
    }
    resp=do_post(payload)
    assert resp.status_code == 400

def test_get_request_found_response_OK():
    do_delete('?application_id=900')
    payload={"application_id": 900,"session_id": "aaaa","message_id": "bbbb","participants": ["avi aviv", "moshe cohen"], "content": "Hi, how are you today?"}
    do_post(payload)
    resp=do_get('?application_id=900')
    assert resp.status_code == 200
    assert resp.json()[0]["application_id"]==900
    

def test_get_request_not_found_response_OK():
    do_delete('?application_id=901')
    resp=do_get('?application_id=901')
    assert resp.status_code == 200
    

def test_get_two_requests_one_found_response_OK():
    do_delete('?application_id=900')
    do_delete('?application_id=901')
    payload={"application_id": 900,"session_id": "aaaa","message_id": "bbbb"  }
    do_post(payload)
    payload={"application_id": 901,"session_id": "aaaa","message_id": "bbbb"  }
    do_post(payload)
    resp=do_get('?application_id=900')
    assert resp.status_code == 200
    assert len(resp.json())==1
    assert resp.json()[0]["application_id"]==900

def test_get_request_with_no_param_bad_request():
    do_delete('?application_id=900')
    payload={"application_id": 900,"session_id": "aaaa","message_id": "bbbb"  }
    do_post(payload)
    resp=do_get('')
    assert resp.status_code == 400

def test_get_request_with_no_value_in_param_bad_request():
    do_delete('?application_id=900')
    payload={"application_id": 900,"session_id": "aaaa","message_id": "bbbb"  }
    do_post(payload)
    resp=do_get('?application_id=')
    assert resp.status_code == 400

def test_get_request_with_not_numeric_value_in_application_param_bad_request():
    payload={"application_id": 900,"session_id": "aaaa","message_id": "bbbb"  }
    do_post(payload)
    resp=do_get('?application_id=abc')
    assert resp.status_code == 400

def test_delete_request_with_no_matching_data_response_not_found():
    resp=do_delete('?application_id=905')
    assert resp.status_code == 404

def do_post(payload):
    url= 'http://127.0.0.1:5000//AddMessage'
    headers = {'Content-Type': 'application/json' } 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    return resp

def do_get(str):
    url= 'http://127.0.0.1:5000//GetMessage'+str
    headers = {'Content-Type': 'application/json' } 
    resp = requests.get(url, headers=headers)       
    return resp

def do_delete(str):
    url= 'http://127.0.0.1:5000//DeleteMessage'+str
    headers = {'Content-Type': 'application/json' } 
    resp = requests.delete(url, headers=headers)       
    return resp



    