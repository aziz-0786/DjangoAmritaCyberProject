from celery import shared_task
import time
import random
from django.core.mail import send_mail
from .models import EvaluationRequest

@shared_task
def process_evaluation_request(request_id):
    try:
        evaluation = EvaluationRequest.objects.get(id=request_id)
        time.sleep(5)  # Simulating evaluation delay
        evaluation.result = f"Generated output: {random.choice(['Positive', 'Negative', 'Neutral'])}"
        evaluation.status = "completed"
        evaluation.save()

        send_mail(
            subject="Evaluation Completed",
            message=f"Your evaluation request (ID: {request_id}) has been completed. Result: {evaluation.result}",
            from_email="noreply@example.com",
            recipient_list=["user@example.com"],
            fail_silently=True,
        )
    except EvaluationRequest.DoesNotExist:
        pass
