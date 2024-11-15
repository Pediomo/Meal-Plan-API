from fastapi import FastAPI
from app.main import app  # Imports the FastAPI app from your app directory

# Vercel expects a function named `handler` to handle incoming requests
def handler(request):
    return app(request)

