from django.shortcuts import render

# Creating views for the profile API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timezone
import requests
import os
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def welcome(request):
    data = {
        "message": "Welcome to HNG Stage 0 Profile API",
        "endpoints": {
            "profile": "/me"
        },
        "documentation": "Visit /me to get profile information with a dynamic cat fact" 
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET']) #fix missing decorator
def profile_endpoint(request):
    cat_fact = "Unable to fetch cat at this time"

    try:
        #Fetch cat Fact
        cat_api_url = os.getenv('CAT_FACT_API_URL', 'https://catfact.ninja/fact')
        timeout = int(os.getenv('CAT_FACTS_API_TIMEOUT', 5))

        cat_response = requests.get(cat_api_url, timeout=timeout)
        cat_response.raise_for_status()
        cat_data = cat_response.json()
        cat_fact = cat_data.get('fact', 'No fact available')

    except request.exceptions.Timeout:
        logger.error("Cat Facts API timeout", exc_info=True)
    except requests.exceptions.RequestException as e:
        logger.error(f"Cat Facts API error: {e}", exc_info=True)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
    

    # Build Response
    data = {
        "status": "success",
        "user": {
            "email": "kimukuphilip10@gmail.com",
            "name": "Philip Kimuku",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
        "fact": cat_fact
    }

    return Response(data, status=status.HTTP_200_OK)
