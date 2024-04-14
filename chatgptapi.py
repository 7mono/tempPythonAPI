import json
import openai

def chatGPTAPI(myquestion):
   client = openai.OpenAI(api_key='CHATGP_TAPI_KEY')
   chat_completion = client.chat.completions.create(
      #messages=[f{"role": "user", "content":"Pythonは好きですか？"}],
      messages=[{"role": "user", "content":myquestion }],
      model="gpt-3.5-turbo",
   )
   content = chat_completion.choices[0].message.content
   print(content)
   return content
