from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json

def create_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        age = data.get("age")

        autobiography = f"My name is {name}. I am {age} years old."

        return JsonResponse({
            "name": name,
            "age": age,
            "autobiography": autobiography
        })

    return JsonResponse({"error": "Invalid request"}, status=400)
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "🚀 Probability Autobiography API is running successfully!"
    })
