from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import EvaluationRequest
from .tasks import process_evaluation_request

@csrf_exempt
def submit_evaluation_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_prompt = data.get("input_prompt")
        if not input_prompt:
            return JsonResponse({"error": "Input prompt is required"}, status=400)

        evaluation = EvaluationRequest.objects.create(input_prompt=input_prompt)
        process_evaluation_request.delay(evaluation.id)

        return JsonResponse({"id": evaluation.id, "status": evaluation.status})
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def retrieve_evaluation_result(request, request_id):
    try:
        evaluation = EvaluationRequest.objects.get(id=request_id)
        return JsonResponse({"id": evaluation.id, "status": evaluation.status, "result": evaluation.result})
    except EvaluationRequest.DoesNotExist:
        return JsonResponse({"error": "Evaluation request not found"}, status=404)
