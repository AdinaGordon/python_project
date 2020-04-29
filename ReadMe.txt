README 
The project implements the following api functions:

POST / AddMessage
URL example: http://127.0.0.1:5000//AddMessage

    Request
    The message data should be added to the request body in json format 
    for example:
    {       
        application_id: 1,
        session_id: ‘aaaa’,
        message_id: ‘bbbb’,
        participants: [‘avi aviv’, ‘moshe cohen’]
        content: ‘Hi, how are you today?’ 
    }

    The following fields are mandatory:ּּ
        application_id,
        session_id,
        message_id
    The application_id value must be numeric.

    Response
    The response status code for POST will be one of the following:
        200 - If the request was succsessfully saved.
        400 - If the mandatory fields are missing or if the application_id value is not numeric
        500 - If there was an exception in the server 

GET / GetMessage
URL example: 
    http://127.0.0.1:5000//GetMessage?application_id=1
    http://127.0.0.1:5000//GetMessage?session_od=aaaa
    http://127.0.0.1:5000//GetMessage?message_id=bbbb

    Request
    Add a parameter in the URL string to filter the returned results 
    
    The URL parameters can be one of the following:
        applicationId – should return list of messages with a matching application id.
        sessionId – should return list of messages with a matching session id.
        messageId– should return a single message with the message id.

    The application_id parameter must be numeric.

    Response
    The response status code will be one of the following:
        200 - If the query was successful even if no results were found.
        400 - If there is no parameter in URL or the application_id value is not numeric.
        500 - If there was an exception in the server. 

DELETE / DeleteMessage
Url example: 
    http://127.0.0.1:5000//DeleteMessage?application_id=1
    http://127.0.0.1:5000//DeleteMessage?session_id=aaaa
    http://127.0.0.1:5000//DeleteMessage?message_id=bbbb

    Request
    Send a URL parameter according to the data you want to delete 
    
    URL paramters should be one of the following:
           applicationId – delete all messages with the application Id.
           sessionId – delete all messages with the session Id.
           messageId– delete a single message with the message Id.

    The _application_id parameter must be numeric.

    Response
    The response status code will be one of the following:
        200 - If the request was succsessfully deleted .
        400 - If there is no parameter in URL or the application_id value is not numeric
        404 - If there is no data matching the URL parameter
        500 - If there was an exception in the server 

    Project pre requirements,
        Python 3 installation ,
        Flask microframework installation.

    How to run
        Copy the files to a folder 
        The DB file used by the Project will be created automatically on the first request
        Open a command window in the files location
        Run the following command : python webapi.py
        Once the server is running requests can be posted using the Url displayed in the command window.










