from fastapi import APIRouter
from api.model_obat import obat 
from api.db import conn 
from api.schema_obat import serializeDict, serializeList
from bson import ObjectId
obat = APIRouter() 

@obat.get('/')
async def find_all_obat():
    return serializeList(conn.users.obat.find())

@obat.get('/{id}')
async def find_one_obat(id):
    return serializeDict(conn.local.obat.find_one({"_id":ObjectId(id)}))

@obat.post('/')
async def create_obat(obat: obat):
    conn.users.obat.insert_one(dict(obat))
    return serializeList(conn.users.obat.find())

@obat.put('/{id}')
async def update_obat(id,obat: obat):
    conn.users.obat.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(obat)
    })
    return serializeDict(conn.users.obat.find_one({"_id":ObjectId(id)}))

@obat.delete('/{id}')
async def delete_obat(id,obat: obat):
    return serializeDict(conn.users.obat.find_one_and_delete({"_id":ObjectId(id)}))
