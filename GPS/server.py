from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import geocoder

# 1. Initialize the FastAPI app
app = FastAPI(title="My First REST API")

def gps_process():
    g = geocoder.ip('me')
    latitude  =  g.latlng[0]
    longitude =  g.latlng[1]
    return latitude, longitude


@app.get("/gps")
def gps():
    lat, long = gps_process()
    return {
        "latitude": lat,
        "longitude": long
    }