#import os
from typing import List
from fastapi import FastAPI, Query, HTTPexceptions
from fastapi.middleware.cors import CORSMiddleware 
import httpx
import uvicorn as uvicorn
from openf1_client import OpenF1Client
from dotenv import load_dotenv


# Alright so this is just a simple backend for an AI F1 telemetry app, 
# it will fetch data from OPENF1 and send it to the frontend for visualization. 
# The goal of this tool is to show data visualization and analysis using AI because AI is the future and it's best to stay up to date with the latest technology.


load_dotenv() # Loads the environment variables from the .env file
app = FastAPI(title="AI F1 Telemetry API", description="An API for fetching F1 telemetry data from OPENF1 and sending it to the frontend for visualization.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

OPENF1_BASE_URL = "https://api.openf1.org/v1"  # Base URL for the OPENF1 API