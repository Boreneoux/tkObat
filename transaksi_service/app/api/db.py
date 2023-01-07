from pymongo import MongoClient
conn = MongoClient('mongodb://root:p455w0rd@172.20.177.16/transactions?authSource=admin')
dbObat= MongoClient('mongodb://root:p455w0rd@172.20.177.16/obats?authSource=admin')
dbUser= MongoClient('mongodb://root:p455w0rd@172.20.177.16/users?authSource=admin')
