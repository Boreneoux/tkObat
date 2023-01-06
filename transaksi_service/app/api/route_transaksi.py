from fastapi import APIRouter
from api.model_transaksi import transaksi 
from api.db import conn 
from api.schema_transaksi import serializeDict, serializeList
from bson import ObjectId
transaksi = APIRouter() 

# localhost -> GET

@transaksi.get('/')
async def find_all_transaksi():
    return serializeList(conn.users.transaksi.find())

# localhost/{T001} -> GET 

@transaksi.get('/{id}')
async def find_one_transaksi(id):
    return serializeDict(conn.local.transaksi.find_one({"_id":ObjectId(id)}))

@transaksi.post('/')
async def create_transaksi(transaksi: transaksi):
    conn.users.transaksi.insert_one(dict(transaksi))
    return serializeList(conn.users.transaksi.find())

@transaksi.put('/{id}')
async def update_transaksi(id,transaksi: transaksi):
    conn.users.transaksi.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(transaksi)
    })
    return serializeDict(conn.users.transaksi.find_one({"_id":ObjectId(id)}))

@transaksi.delete('/{id}')
async def delete_transaksi(id,transaksi: transaksi):
    return serializeDict(conn.users.transaksi.find_one_and_delete({"_id":ObjectId(id)}))
