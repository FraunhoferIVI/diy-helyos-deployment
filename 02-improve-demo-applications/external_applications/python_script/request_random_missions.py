import random, time
from helyos_requests import get_free_agents, create_work_process

# Define the GraphQL endpoint and headers
hostname = "https://helyos-server.ivi.fraunhofer.de"
port = 5000
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoicm9sZV9hcHBsaWNhdGlvbiIsInBlcnNvbl9pZCI6bnVsbCwiZXhwIjoxNzY0NzYxNDU3LCJpYXQiOjE3MzMyMjU0NTYsImF1ZCI6InBvc3RncmFwaGlsZSIsImlzcyI6InBvc3RncmFwaGlsZSJ9.Hzqf1npJZwt49pXOyS77hAd4lpsdFnK1trmPveYnBE4"
}
graphql_conf = { 'url': f"{hostname}:{port}/graphql", 'headers': headers }

# Main function to request a random mission for a random free agent
def request_random_mission():
    free_agents = get_free_agents(graphql_conf)
    if not free_agents:
        return
    
    # Randomly select a free agent
    for selected_agent in free_agents:
        agent_uuid = selected_agent['uuid']
        agent_yard_id = selected_agent['yardId']
        current_pos =  {'x':selected_agent['x'],
                        'y':selected_agent['y'], 
                        'orientations':selected_agent['orientations']}
        
        random_destination = { 'x':random.randint(-10000, 10000),
                        'y':random.randint(-20000, 20000), 
                        'orientations':[random.randint(-6000, 6000)]}

        request_data = {'agent_uuid': agent_uuid,
                        'initial_position': current_pos,
                        'destination': random_destination}
        
        # Create a work process (mission) for the selected agent
        mission = create_work_process(graphql_conf,agent_uuid, agent_yard_id, "driving", request_data)
        print(f"Mission created with ID: {mission['id']} for Agent UUID: {agent_uuid}")

# Execute the main function
try:
    print("This command will repeat until you press Control + C")
    while True:
        time.sleep(2)
        request_random_mission()
except KeyboardInterrupt:
    print("Loop interrupted by user.")
