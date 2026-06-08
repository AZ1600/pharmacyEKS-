from fastapi import APIRouter
from app.models.drug import DrugRequest
from app.services.drug_service import create_drug_service

router = APIRouter()

def get_claims():
    return {
        "custom:role": "HospitalAdmin",
        "custom:tenant_id": "tenant_001",
        "sub": "user_123"
    }

@router.post("/drugs")
def create_drug(drug: DrugRequest):

    claims = get_claims()
    tenant_id = claims["custom:tenant_id"]
    user_id = claims["sub"]

    return create_drug_service(drug, tenant_id, user_id)