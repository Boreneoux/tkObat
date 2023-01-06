def obatEntity(item) -> dict:
    return {
        "kd_obat":str(item["kd_obat"]),
        "nama_obat":item["nama_obat"],
        "jenis_obat":item["jenis_obat"],
        "harga":item["harga"],
        "stok": item["stok"]
    }

def obatEntity(entity) -> list:
    return [obatEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
