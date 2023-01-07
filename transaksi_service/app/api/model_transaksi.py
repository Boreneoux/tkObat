from pydantic import BaseModel

class Transaksi(BaseModel):
    # id = id nya dari db user -> id transaksi ada lagi cek di schema
    id: str
    kd_obat: str
    quantity: int
    nama_obat: str
    jenis_obat: str
    harga: int
    stok: int
    total: int