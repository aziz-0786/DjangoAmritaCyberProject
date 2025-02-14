#Django LLM Evaluation Backend

#Overview

This project is a backend service built using Django and PostgreSQL that simulates an evaluation pipeline for an LLM application. The service exposes REST API endpoints to submit evaluation requests, process them asynchronously using Celery, and store/retrieve results. Upon task completion, an email notification is sent using the Resend API.

#Features

REST API to submit and retrieve evaluation requests.

Asynchronous task processing using Celery and Redis.

PostgreSQL for data storage.

Email notifications using the Resend API.

Docker support for easy deployment.

#Prerequisites

Ensure you have the following installed:

Python 3.8+

PostgreSQL

Redis (for Celery task queue)

Docker (optional for containerized deployment)

#Installation

1. Clone the Repository
   git clone https://github.com/aziz-0786/DjangoAmritaCyberProject.git
2. Create a Virtual Environment
      venv\Scripts\activate
3. Install Dependencies
       pip install -r requirements.txt
      
4. Configure Database

#Update backend/settings.py with your PostgreSQL credentials:

   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#Run migrations:
python manage.py migrate

5. Start Redis (for Celery)
   redis-server
6. Start Celery Worker
   celery -A backend worker --loglevel=info
7. Run Django Server
   python manage.py runserver

   
#API Endpoints

#Submit Evaluation Request
POST /api/evaluate/
Content-Type: application/json
{
    "input_prompt": "Test LLM"
}

#Retrieve Evaluation Result
GET /api/evaluate/{id}/

#Docker Deployment
#Build and Run
   docker-compose up --build


