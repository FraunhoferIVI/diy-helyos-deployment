import requests
import json


# Function to perform a GraphQL request
def graphql_request(graphql_conf, query, variables=None):
    payload = {
        "query": query,
        "variables": variables
    }
    response = requests.post(graphql_conf['url'], json=payload, headers=graphql_conf['headers'])
    response.raise_for_status()
    return response.json()

# Function to retrieve all free agents
def get_free_agents(graphql_conf):
    query = """
    query allAgents($condition: AgentCondition!) {
        allAgents(condition: $condition) {
            nodes { id, uuid, yardId, x, y, orientations }
        }
    }
    """
    condition = {"status": "free"}
    variables = {"condition": condition}
    result = graphql_request(graphql_conf, query, variables)
    return result['data']['allAgents']['nodes']

# Function to create a work process (mission) for an agent
def create_work_process(graphql_conf, agent_uuid, yard_id, work_process_type_name, request_data):
    mutation = """
    mutation createWorkProcess($postMessage: CreateWorkProcessInput!) {
        createWorkProcess(input: $postMessage) {
            workProcess {id, status}
        }
    }
    """
    variables = {
        "postMessage": {
            "workProcess": {
                "status": "dispatched",
                "data": json.dumps(request_data),
                "yardId": yard_id,
                "workProcessTypeName": work_process_type_name,
                "agentUuids": [agent_uuid]
            }
        }
    }
    result = graphql_request(graphql_conf, mutation, variables)
    return result['data']['createWorkProcess']['workProcess']
