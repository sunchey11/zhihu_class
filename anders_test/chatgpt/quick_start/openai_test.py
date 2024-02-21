from openai import OpenAI
from utils.Utils import initClient

# https://platform.openai.com/docs/quickstart/step-3-sending-your-first-api-request
# client = OpenAI()
client = initClient()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)