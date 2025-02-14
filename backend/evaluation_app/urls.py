from django.urls import path
from .views import submit_evaluation_request, retrieve_evaluation_result

urlpatterns = [
    path('evaluate/', submit_evaluation_request, name='submit_evaluation_request'),
    path('evaluate/<int:request_id>/', retrieve_evaluation_result, name='retrieve_evaluation_result'),
]
