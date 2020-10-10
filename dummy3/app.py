import pymysql 
from flask import Flask 
from flask_restful import Resource, Api 
from flask_restful import reqparse 


app = Flask(__name__)
api = Api(app)

class KillUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_name', type=str)
            args = parser.parse_args()
            _userName = args['user_name']

            conn = pymysql.connect(host='164.125.219.21', port=13306, user='root', password='test1234', database='junction_zepia')
            cursor = conn.cursor()
            sql ="UPDATE user SET isalive=0 WHERE username=%s"
            cursor.execute(sql, (_userName,))
            conn.commit() 

            return {'StatusCode': '200', 'Message': 'User Killing Success'}

        except Exception as e:
            return {'error': str(e)}

class LogIn(Resource):
    def post(self):
         try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userName = args['user_name']
            _passWord = args['password']
            
            conn = pymysql.connect(host='164.125.219.21', port=13306, user='root', password='test1234', database='junction_zepia')
            cursor = conn.cursor()
            sql = "SELECT * FROM user WHERE username=%s and password=%s"
            cursor.execute(sql, ( _userName, _passWord))
            num = cursor.rowcount

            if num==1:
                return {'StatusCode' : '200' , 'Message': 'LogIn Success'}
            else: 
                return {'StatusCode' : '400', 'Message' : 'LogIn Fail'}
         except Exception as e:
            return {'error': str(e)}



api.add_resource(KillUser, '/killuser') 
api.add_resource(LogIn, '/login')

if __name__ == '__main__':
    app.run(debug=True, port=3000)

