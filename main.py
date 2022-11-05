from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import models

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def fetch_profile():
    return {
        "slackUsername": "Emmanuel Simasiku",
        "backend": True,
        "age": 30,
        "bio": "I'm an enthusiastic software developer with a particular passion for Backend development."
    }


@app.post("/arithmetics/", response_model=models.OutputModel)
def perform_arithmetics(data: models.InputModel):
    request_data = data.dict()
    operation_type = request_data['operation_type']
    x = request_data['x']
    y = request_data['y']

    operations = ['addition', 'subtraction', 'multiplication']

    if operation_type in operations:
        if operation_type == 'addition':
            result = x + y
        
        elif operation_type == 'subtraction':
            result = x - y

        else:
            result = x * y

        response = {
            "slackUsername": "Emmanuel Simasiku",
            "result": result,
            "operation_type": operation_type
        }

        return response

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, details='Invalid operation type')
