# Smart Task Manager API

## Overview
The Smart Task Manager API allows users to manage their tasks effectively. It supports creating, retrieving, updating, and deleting tasks.

## Features
- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update a task
- Delete a task
- Task suggestions and due date prediction

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- MySQL

### Installation

1. Clone the repository:
   git clone https://github.com/your-username/smart-task-manager-api.git
   cd smart-task-manager-api

2. python -m venv venv

3. venv\Scripts\activate

4. pip install -r requirements.txt

5. Set up the database:
  Update the DATABASES setting in settings.py to connect to your MySQL database.

6. python manage.py migrate

7. python manage.py runserver

8. Create a task:
   curl -X POST http://127.0.0.1:8000/tasks/ -H "Content-Type: application/json" -d '{"title": "Task 1", "description": "Description", "due_date": "2024-10-10", "completed": false}'

9. Update a task:
    curl -X PUT http://127.0.0.1:8000/tasks/{id}/ -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated description", "due_date": "2024-10-20", "completed": false}'

10. Delete a task:
    curl -X DELETE http://127.0.0.1:8000/tasks/{id}/

11. 
