from fastapi import FastAPI
from app.chatbot import chatbot_router

app = FastAPI()

app.include_router(chatbot_router, prefix="/chatbot", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blockchain Courses API"}
