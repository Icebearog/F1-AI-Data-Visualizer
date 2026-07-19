import os
from dotenv import load_dotenv
from typing import List
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
import httpx
#import pandas as pd
from urllib.request import urlopen
import json



# Alright so this is just a simple backend for an AI F1 telemetry app, 
# it will fetch data from OPENF1 and send it to the frontend for visualization. 
# The goal of this tool is to show data visualization and analysis using AI because AI is the future and it's best to stay up to date with the latest technology.


load_dotenv() 
app = FastAPI(title="AI F1 Telemetry API", description="An API for fetching F1 telemetry data from OPENF1 and sending it to the frontend for visualization.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

response = urlopen(os.getenv("OPENF1_BASE_URL"))
data = json.loads(response.read().decode('utf-8'))
print(data)


app.get("/api/sessions/compare")
async def compare_sessions(
        session_key: int = Query(..., description="The session ID"),
        drivers: List[int] = Query(..., description="List of driver numbers to compare")
):
    """
    Fetches lap data from OpenF1 and structures it cleanly for frontend charting.
    Ensures O(n) complexity during data processing.
    """
app.get("/")
