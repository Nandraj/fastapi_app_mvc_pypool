from fastapi import APIRouter, HTTPException
from app.models import PayLoadModel, ResponseModel
from app.controllers import process_payload, logging
from datetime import datetime, timezone
import logging

logging.basicConfig(
    filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

api_router = APIRouter()


@api_router.post("/process", response_model=ResponseModel)
async def process(payload: PayLoadModel):
    try:
        started_at = datetime.now(timezone.utc)
        result = process_payload(payload.payload)
        completed_at = datetime.now(timezone.utc)
        response = ResponseModel(
            batchid=payload.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at,
        )
        return response
    except Exception as e:
        logging.error(f"Error in /process endpoint : {e}")
        raise HTTPException(status_code=500, detail=str(e))
