from flask import Flask 
from flask_restful import Resource, Api 
from flask_restful import reqparse 
from flaskext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test1234'
app.config['MYSQL_DATABASE_DB'] = 'junction_zepia'
app.config['MYSQL_DATABASE_HOST'] = '164.125.219.21'
app.config['MYSQL_DATABASE_PORT'] = 13306
mysql.init_app(app)


class KillUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_name', type=str)
            parser.add_argument('dummy', type=str)
            args = parser.parse_args()

            _userName = args['user_name']
            _dummy = args['dummy']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_kill_user_2', (_userName, _dummy))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User Killing success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}


api.add_resource(KillUser, '/killuser') 

if __name__ == '__main__':
    app.run(debug=True)

