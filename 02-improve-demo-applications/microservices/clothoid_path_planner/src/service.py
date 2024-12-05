from flask import Flask, jsonify,  request
from path_calculation import calculate_path

app = Flask(__name__)

@app.post("/plan_job/")
def getPath():
    """
    Calculate path using a data format COMPATIBLE with the AGENT.
    """
    request_body = request.get_json() 
    request_data = request_body['request']   # Input from external application.
    helyos_context = request_body['context'] # Snapshot from helyos database.

    # Parse input data
    agent_uuid = request_data.get('agent_uuid',  None)
    initial_position = request_data.get('initial_position', None) 
    destination = request_data.get('destination', initial_position) 

    # Calculate path
    assignment = calculate_path(initial_position, destination)
 
    # Return response
    response =     {
                    "results":[{
                                    "agent_uuid": agent_uuid,
                                    "assignment": assignment
                                }]
                }
    

    return jsonify(response)

# We do not need this because we are using gunicorn to run "app"
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9002, debug=True)



