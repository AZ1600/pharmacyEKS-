from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "pharmacy-api running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)