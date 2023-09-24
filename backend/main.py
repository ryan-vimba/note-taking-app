from fastapi import FastAPI
from starlette.config import Config
from starlette.requests import Request
from database import SessionLocal, get_or_create_user
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from google.oauth2 import id_token
from google.auth.transport import requests
import httpx

app = FastAPI()


config = Config('.env')
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = config('GOOGLE_REDIRECT_URI')
SECURE_KEY = config('SECURE_KEY')

origins = [
    "http://localhost:3000",
]

app.add_middleware(SessionMiddleware, secret_key=SECURE_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/auth")
async def auth(request: Request, code: str):
    # URL to exchange code for access token
    token_endpoint = 'https://oauth2.googleapis.com/token'

    # Payload contains the details for the POST request
    payload = {
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'code': code,
        'redirect_uri': "postmessage",
        'grant_type': 'authorization_code'
    }

    # Make the POST request to get the tokens
    response = httpx.post(token_endpoint, data=payload)
    token_data = response.json()
    print(token_data)
    print(response)

    # Extract the access token and ID token
    access_token = token_data.get('access_token')
    id_token_str = token_data.get('id_token')

    # Verify the ID token
    id_info = id_token.verify_oauth2_token(id_token_str, requests.Request(), GOOGLE_CLIENT_ID)
    
    if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')
    
    # Save the email to the session or do something else
    request.session['user'] = {
        "email": id_info["email"]
    }

    return {"message": "Successfully authenticated"}


@app.get('/')
def check(request:Request):
    user = request.session.get('user')
    if not user:
        return {"error": "Not authenticated"}
    return "hi "+ str(request.session.get('user')['email'])
