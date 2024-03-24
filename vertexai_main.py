import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def generate():
  model = GenerativeModel("gemini-pro-vision")
  responses = model.generate_content(
    """I need to create a recommendation engine for my customers where their profiles will be matched with company profiles according to their investment preferences. Walk me through how I can create one, including but not limited to which data I should procure, the features I need to consider, DB where I can store the matches, the recommendation model, etc. I want to use Gemini Pro Vision for the recommendation engine, but I don't have historical data. Give code, pls.""",
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32
    },
  stream=True,
  )
  
  for response in responses:
      print(response.candidates[0].content.parts[0].text)


generate()