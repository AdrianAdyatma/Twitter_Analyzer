import pymongo
import mysql.connector

# MySQL Database identifier & connection
sql_db_name = "tweets_db"
sqlDb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database=sql_db_name
)
sqlCursor = sqlDb.cursor()

# MongoDB Database identifier & connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
TwitterDB = client.TwitterDB
# TwitterDB = client.NewTwitterDB
tweets = TwitterDB.tweets

# Find all tweets
find_all = tweets.find()

# Find unprocessed tweets
unprocessed = {"processed": False}
find_unprocessed = tweets.find(unprocessed)
