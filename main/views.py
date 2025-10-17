from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from datetime import datetime
from rest_framework.throttling import AnonRateThrottle


class ProfileApiView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]
    def get(self, request):
        name = "Nwosisi Ebuka Stephen"
        email = "sebuka559@gmail.com"
        stack = "Python/Django"

        try:
            url = "https://catfact.ninja/fact"
            response = requests.get(url, timeout=5)  
            response.raise_for_status()
            cat_fact = response.json().get("fact", "No fact available")
        except requests.exceptions.RequestException as e:
            return Response(
                {
                    "status": "error",
                    "message": "Failed to fetch cat fact",
                    "details": str(e),
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {
                "status": "success",
                "data": {
                    "name": name,
                    "email": email,
                    "stack": stack,
                },
                "timestamp": datetime.utcnow().isoformat(),
                "fact": cat_fact,
            },
            status=status.HTTP_200_OK,
        )
