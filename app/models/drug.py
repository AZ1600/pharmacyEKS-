from pydantic import BaseModel

class DrugRequest(BaseModel):
    drug_name: str
    batch_number: str
    quantity: int
    reorder_level: int
    expiry_date: str
    supplier: str | None = ""