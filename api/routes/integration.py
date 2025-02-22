from fastapi import APIRouter, Request, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

router = APIRouter()

class TelexSetting(BaseModel):
    label: str
    type: str
    required: bool
    default: str


class TelexPayload(BaseModel):
    channel_id: str
    return_url: str
    settings: list[TelexSetting]


#telex integration.json endpoint
@router.get("/integration.json")
def integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {
                "created_at": "2025-02-21",
                "updated_at": "2025-02-21"
                },
            "descriptions": {
                "app_name": "Pheidippides API",
                "app_description": "An integration that suggests books to read based on any selected genre.",
                "app_logo": "https://i.imgur.com/D2619X4.jpeg",
                "app_url": f"{base_url}", #change to an env variable
                "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "interval",
            "integration_category": "Communication & Collaboration",
            "key_features": [
                "daily-book-recommendations"
                ],
            "author": "Ayodeji Oni",
            "settings": [
                {
                    "label": "genre",
                    "type": "dropdown",
                    "required": True,
                    "default": "random",
                    "options": [
                        "random",
                        "fantasy",
                        "mystery",
                        "horror",
                        "romance",
                        "dystopian",
                        "adventure",
                        "biography",
                        "history",
                        "comedy",
                        "nigerian"
                        ]
                },
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "default": "* * * * *"
                }
            ],
            # "target_url": "\"\"",
            "tick_url": f"{base_url}/tick" #change to an env variable
        }
    }

#Implemetations to get genre from request payload

#telex tick_url endpoint
@router.post("/tick")
def tick_url():
    return {"tick url status": "Healthy"}