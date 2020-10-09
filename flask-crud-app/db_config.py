from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config[‘MYSQL_DATABASE_USER’] = ‘root’
app.config[‘MYSQL_DATABASE_PASSWORD’] = ‘test1234’
app.config[‘MYSQL_DATABASE_DB’] = ‘test’
app.config[‘MYSQL_DATABASE_HOST’] = 164.125.219.21
mysql.init_app(app)
