import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LifeProfile

@csrf_exempt
def create_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)

        profile = LifeProfile.objects.create(
            name=data["name"],
            age=data["age"],
            profession=data["profession"],
            probability=42
        )

        return JsonResponse({
            "success": True,
            "probability": profile.probability
        })

    return JsonResponse({"error": "Invalid request"}, status=400)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LifeProfile

@csrf_exempt
def create_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # simple probability logic
        probability = min(100, int(data["age"]) * 2)

        profile = LifeProfile.objects.create(
            name=data["name"],
            age=data["age"],
            profession=data["profession"],
            probability=probability
        )

        return JsonResponse({
            "message": "Profile saved successfully",
            "probability": profile.probability
        })

    return JsonResponse({"error": "Invalid request"}, status=400)