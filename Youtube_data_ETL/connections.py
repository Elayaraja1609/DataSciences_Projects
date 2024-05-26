import mysql.connector
from googleapiclient.discovery import build
import sqlalchemy

# local MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="youtube_data"
)
my_sql_cursor = mydb.cursor(buffered=True)

sql_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format('root', '', 'localhost', 'youtube_data'))

# Youtube API connections details
api_key = ""

youtube = build('youtube','v3',developerKey=api_key)