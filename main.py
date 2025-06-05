from fastapi import FastAPI
from routes.analyse_comments import router as analyse_comments_router
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def base_route():
    return {"message": "This is the homepage of the sentiment analysis app."}

# Mount your routes
app.include_router(analyse_comments_router, prefix="/comments")
