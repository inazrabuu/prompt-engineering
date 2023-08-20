def get_completion(openai, prompt, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=0, 
  )
  return response.choices[0].message["content"]

def temperature_completion(openai, prompt, model="gpt-3.5-turbo", temperature=0):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=temperature, 
  )
  return response.choices[0].message["content"]

def get_completion_from_messages(openai, messages, model="gpt-3.5-turbo", temperature=0):
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=temperature, # this is the degree of randomness of the model's output
  )

  return response.choices[0].message["content"]

def o(message):
  return f"""
    hello {message}
    """