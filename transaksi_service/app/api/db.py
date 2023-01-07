from pymongo import MongoClient
conn = MongoClient('mongodb://root:p455w0rd@172.20.187.81/transactions?authSource=admin')
dbObat= MongoClient('mongodb://root:p455w0rd@172.20.187.81/obats?authSource=admin')
dbUser= MongoClient('mongodb://root:p455w0rd@172.20.187.81/users?authSource=admin')
