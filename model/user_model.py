import mysql.connector
import json
from flask import jsonify
from flask import make_response

from dotenv import load_dotenv
import os
load_dotenv()

host = os.getenv("HOST")
user = os.getenv("ROOT")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

class User_model:
    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host=host, 
                user=user, 
                password=password, 
                database=database
            )
            self.conn.autocommit=True
            self.cur = self.conn.cursor(dictionary=True)
            print("connection successful")
        except mysql.connector.Error as e:
            self.conn = None
            self.cur = None
            print(f"Connection error: {e}")

    def user_getall_model(self):
        if self.cur is None:
            return json.dumps({"error": "Database connection failed"})

        query = "SELECT * FROM users"
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
            # return jsonify(result)
            # return make_response({'payload':result}, 200)
            res = make_response({'payload': result}, 200)
            res.headers['Acces-Control-Allow-Origin'] = '*'   # if the FE is at different origin than BE means BE and FE are at different servers
            return res
        
        except mysql.connector.Error as e:
            # return json.dumps({"error": str(e)})
            return make_response({'message': 'no data found'}, 204)


    def user_addone_model(self, data):
            query = f"INSERT INTO users (user, email, phone, role, password) VALUES ('{data['user']}', '{data['email']}', '{data['phone']}', '{data['role']}','{data['password']}')"
            self.cur.execute(query)
            # result = self.cur.fetchall()
            # return jsonify(result)
            self.conn.commit()

            return make_response({"message": 'this is user_addone_model operation and user created successfully'}, 201)

    def user_update_model(self, data):
            query = f"UPDATE users SET user = '{data['user']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id ={data['id']} "
            self.cur.execute(query)
            if self.cur.rowcount>0:
                 return make_response({'message':'user updated successfully'}, 201)
            else:
                 return make_response({'message':'nothing updated'}, 202)
           
    def user_delete_model(self, id):
            query = f"DELETE from users  WHERE id = {id} "
            self.cur.execute(query)
            if self.cur.rowcount>0:
                 return make_response({'message':'user deleted successfully'}, 201)
            else:
                 return make_response({'message':'nothing to delete'}, 202)
            

    def user_patch_model(self, data, id):
            query = f"UPDATE users SET "
            for key in data:
                 query = query + f"{key}='{data[key]}',"
            query = query[:-1] + f" WHERE id={id}" 
            self.cur.execute(query)
            if self.cur.rowcount>0:
                return make_response({'message':'this is user patch operatoin and user updated successfully'}, 202)
            else:
                 return make_response({"message": "nothing to update"})