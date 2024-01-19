import requests
import json

# Set your OpenAI API key
api_key = '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'

# Headers for API requests
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'OpenAI-Beta': 'assistants=v1'
}

# 1. Create a new thread
thread_response = requests.post('https://api.openai.com/v1/threads', headers=headers)
if thread_response.status_code != 200:
    print("Failed to create a thread:", thread_response.text)
    exit()

thread_id = thread_response.json()['id']

# 2. Send a message using the Runs API
run_data = {
    'assistant_id': 'asst_gxKUZBSdGdrgZZZ9z4fNWIOu',
    'instructions': 'Is it possible to create new commands that are callable via eval in a test case?'
}
run_response = requests.post(f'https://api.openai.com/v1/threads/{thread_id}/runs', headers=headers, data=json.dumps(run_data))
if run_response.status_code != 200:
    print("Failed to send a message:", run_response.text)
    exit()
print (run_response.text)
run_id = run_response.json()['id']

# 3. Retrieve the Assistant's Response
retrieve_run_response = requests.get(f'https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}', headers=headers)
if retrieve_run_response.status_code != 200:
    print("Failed to retrieve the response:", retrieve_run_response.text)
    exit()

print(retrieve_run_response.json())
