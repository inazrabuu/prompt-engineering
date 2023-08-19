def get_completion(openai, prompt, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=0, 
  )
  return response.choices[0].message["content"]

def o(message):
  return f"""
    hello {message}
    """