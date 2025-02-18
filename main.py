from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

# FastAPI instance creation
app = FastAPI(
    title="pheidippedes-api",
    summary="An output integrationn designed for telex",
    version="0.1.0")

class Payload(BaseModel):
    event_name: str = "string"
    message: str = "python post"
    status: str = "success"
    username: str = "Ayodeji"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

telex_channel_url = "https://ping.telex.im/v1/webhooks/0195057a-ebc9-7646-af52-41800fa80490"

@app.get("/")
async def root():
    return {
        "author": "Ayodeji Oni",
        "api": "pheiddipedes"
    }

async def telex(payload_data: Payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            telex_channel_url,
            json=payload_data,
            headers={
                "Accept" : "application/json",
                "Content-Type" : "application/json"
                }
        )

        return response


# @app.post("/pheidippedes")
# async def test_webhook(post_payload: Payload):
#     return {"message": "Webhook sent successfully"}

@app.post("/pheidippedes")
async def test_webhook(post_payload: Payload):
    try:
        response = await telex(post_payload)
        return {"message": "Webhook sent successfully", "response" : response}
    except Exception as e:
        return {"message": "Webhook failed", "error": e}


