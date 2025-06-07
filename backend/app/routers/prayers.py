from fastapi import APIRouter, Query, HTTPException
from app.services.aladhan import get_prayer_times
from typing import Dict, Any
import httpx

router = APIRouter(
    prefix="/api",
    tags=["prayers"]
)

@router.get("/prayers", response_model=Dict[str, Any])
async def get_prayers(
    city: str = Query(..., description="City name (e.g., 'New York', 'London')"),
    country: str = Query(..., description="Country name (e.g., 'USA', 'UK')"),
    method: int = Query(2, description="Calculation method (2 is Islamic Society of North America)")
) -> Dict[str, Any]:
    """
    Get prayer times for a specific city and country.
    
    Args:
        city: The name of the city
        country: The name of the country
        method: The calculation method (default: 2 for ISNA)
    
    Returns:
        Dictionary containing prayer times and date information
    
    Raises:
        HTTPException: If the API request fails or invalid parameters are provided
    """
    try:
        data = await get_prayer_times(city, country, method)
        return data
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch prayer times: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
