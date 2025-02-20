from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/integration")
def integration_json():
    return {"integration status": "Healthy"}


@router.post("/tick")
def tick_url():
    return {"tick url status": "Healthy"}