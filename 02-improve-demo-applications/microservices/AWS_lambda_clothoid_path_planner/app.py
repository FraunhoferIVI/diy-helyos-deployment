from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from path_calculation import calculate_path
from mangum import Mangum

app = FastAPI()

class RequestBody(BaseModel):
    request: dict
    context: dict

@app.post("/plan_job")
async def get_path(request_body: RequestBody):
    """
    Calculate path using a data format COMPATIBLE with the AGENT.
    """
    request_data = request_body.request   # Input from external application.
    helyos_context = request_body.context # Snapshot from helyos database.

    # # Parse input data
    agent_uuid = request_data.get('agent_uuid', None)
    initial_position = request_data.get('initial_position', None)
    destination = request_data.get('destination', initial_position)

    # # Calculate path
    assignment = calculate_path(initial_position, destination)

    # Return response
    response = {
        "results": [{
            "agent_uuid": agent_uuid,
            "assignment": assignment
        }]
    }

    return response

# Create a handler for AWS Lambda
lambda_handler = Mangum(app)