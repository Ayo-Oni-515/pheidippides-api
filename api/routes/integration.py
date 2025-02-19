from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/integration")
def integration_json():
    return {"integration status": "Healthy"}