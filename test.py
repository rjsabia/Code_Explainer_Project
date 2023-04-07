import os
import openai

openai.api_key = os.getenv('OPEN_AI_KEY_01')

prompt1 = "Give me details about the technology startup called Mimi and Pimo"
prompt2 = "Give me details about the technology startup called Mimi and Pimo. Only answer if you are 100% sure that this company exist, otherwise specify, 'I don't know man'"

response = openai.Completion.create(engine='text-davinci-003',
    prompt=prompt1,
    max_tokens=256,
    temperature=0.7)

test = response['choices'][0]['text']
print(test)

# test push for comments