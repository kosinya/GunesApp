import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth.router import router as auth_router
from mail.router import router as mail_router
from media.router import router as media_router

import config

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Authorization", "Access-Control-Request-Headers", "Access-Control-Allow-Headers"],
)

app.mount("/static", StaticFiles(directory=config.STATIC_FOLDER), name="static")
app.include_router(auth_router, prefix="/auth/jwt")
app.include_router(mail_router, prefix="/mail")
app.include_router(media_router, prefix="/media")


@app.get('/')
async def welcome():
    return {"message": "Welcome to JWTauth"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
