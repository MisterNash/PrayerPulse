from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import prayers

app = FastAPI(
    title="PrayerPulse API",
    description="API for retrieving Islamic prayer times",
    version="1.0.0"
)

# Configure CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(prayers.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to PrayerPulse API",
        "docs_url": "/docs",
        "endpoints": {
            "prayer_times": "/api/prayers?city={city}&country={country}"
        }
    }
