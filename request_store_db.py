import sqlite3
from request_data import RequestData 


class RequestStoreDb:
    def __init__(self):
        self.con=sqlite3.connect('request_db.sqlite')
        self.c=self.con.cursor()

        self.c.execute(''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='requests' ''')

        if self.c.fetchone()[0]==0: 
            self.c.execute("""CREATE TABLE requests( application_id integer,
                                         session_id text,
                                         message_id text,
                                         participants text,
                                         content text )""")
            
            self.con.commit()

    def save_request(self, r):
        with self.con:
            participants_string=r.get_participants_as_string()
            self.c.execute("INSERT INTO requests VALUES (:application_id, :session_id, :message_id, :participants, :content)", {'application_id': r.application_id, 'session_id': r.session_id, 'message_id': r.message_id, 'participants': participants_string, 'content': r.content})


    def get_requests(self,r):
        with self.con:
            sql_string='SELECT *'+self.get_sql_by_paramater(r.args)
            self.c.execute(sql_string)            
            data=self.c.fetchall()
            request_list=[]
            for row in data:
                participants=[]
                if row[3]:
                    participants=row[3].split(",")  
                r=RequestData(row[0],row[1],row[2],participants,row[4])
                request_list.append(r)
            return request_list

    def delete_requests(self,r):
        with self.con:
            sql_count='SELECT count(*)'+ self.get_sql_by_paramater(r.args)
            self.c.execute(sql_count)
            if self.c.fetchone()[0]==0: 
                return False
            sql_string='DELETE'+self.get_sql_by_paramater(r.args)
            self.c.execute(sql_string)
        return True
    
    def get_sql_by_paramater(self, args_list):
        sql_string = ''
        if 'application_id' in args_list:
            sql_string = " from requests WHERE application_id=" +  args_list['application_id']
        if 'session_id' in args_list:
            sql_string = " from requests WHERE session_id=" + "'" + args_list['session_id'] + "'"
        if 'message_id' in args_list:
            sql_string = " from requests WHERE message_id=" + "'" + args_list['message_id'] + "'"
        return sql_string 
    








