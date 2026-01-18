from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest

router = APIRouter()

@router.get('/info', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return {"service": "Depression assessment info",   "version": "1.0.0"}



@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return get_depression()

