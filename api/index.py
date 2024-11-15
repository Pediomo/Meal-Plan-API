# api/index.py
from fastapi import FastAPI
from app.main import app  # Imports the FastAPI app 

api = app  # Vercel to use the FastAPI app as the entry point
