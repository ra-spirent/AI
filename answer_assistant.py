import requests
import json
import time
from openai import OpenAI

# Set your OpenAI API key
client=OpenAI(api_key='**********')




thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="iTestRT folder is empty after installing iTest 4.3.1 GUI software. Why?"
#    content="How to configure or check spirent testcenter automation API port?"
#    content="Is it possible to create new commands that are callable via eval in a test case?"
 
)
print("Prompt: " + message.content[0].text.value)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id="********",
)

status="queued"
while status !="completed":
    run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
    )
    status=run.status
    #print(run)
    time.sleep(3)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)
print("Response: " + messages.data[0].content[0].text.value)