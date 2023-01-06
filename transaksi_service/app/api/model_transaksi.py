from pydantic import BaseModel

class Obat(BaseModel):
    id_transaksi: str
    kd_obat: str
    quantity: int
    harga: int
    total: int 