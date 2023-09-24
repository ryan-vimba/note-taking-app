from fastapi import FastAPI, Depends, HTTPException
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.requests import Request
from .database import SessionLocal, get_or_create_user


app = FastAPI()

# Load your Google OAuth2 credentials (You can use environment variables or a config file)
config = Config('.env')
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = config('GOOGLE_REDIRECT_URI')

oauth = OAuth(config)
oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'email profile'}
)

@app.route('/login/')
async def login(request: Request):
    # Generate the Google OAuth2 authorization URL and redirect user
    redirect_uri = GOOGLE_REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.route('/auth/')
async def authorize(request: Request):
    try:
        # Fetch the access token
        token = await oauth.google.authorize_access_token(request)

        # Fetch the user's info using the access token
        user_info = await oauth.google.parse_id_token(request, token)
        
        # Initiate a new DB session
        session = SessionLocal()
        
        # At this point, you can check if this user exists in your database
        email = user_info.get('email')
        name = user_info.get('name')
        
        # If they don't exist, create a new user record
        user = get_or_create_user(session, email, name)
        
        # Close DB session
        session.close()
        
        # You might also want to create a session or JWT token to keep the user logged in

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Successfully authenticated", "user": user_info}
