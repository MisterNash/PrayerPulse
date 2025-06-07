import httpx
from typing import Dict, Any
from datetime import datetime

async def get_prayer_times(city: str, country: str, method: int = 2) -> Dict[str, Any]:
    """
    Get prayer times for a specific city and country using the Aladhan API.
    
    Args:
        city (str): City name
        country (str): Country name
        method (int): Calculation method (2 is Islamic Society of North America)
    
    Returns:
        Dict containing prayer times and date information
    """
    url = "http://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city,
        "country": country,
        "method": method
    }

    headers = {
        "User-Agent": "PrayerPulseApp/1.0"
    }

    async with httpx.AsyncClient(headers=headers, follow_redirects=True) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
        
        # Extract only the relevant prayer times and date
        timings = data["data"]["timings"]
        date = data["data"]["date"]["readable"]
        
        return {
            "date": date,
            "prayer_times": {
                "Fajr": timings["Fajr"],
                "Sunrise": timings["Sunrise"],
                "Dhuhr": timings["Dhuhr"],
                "Asr": timings["Asr"],
                "Maghrib": timings["Maghrib"],
                "Isha":timings["Isha"]
            }
            
        }
        
    