from openai import OpenAI
client = OpenAI(api_key="")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Provide me information about \"Wenzhou Success Group Bags Co. Ltd\" and \"\nLitai (Quanzhou) Bags Corp.,Ltd\" vendor of bags in the following json format: {\"Years in Business\": ,\"user review\":, \"location\": , \"delivery time\":, \"unit\": , \"logistics (managed by)\": } If you can't find any information give it your best guess, then provide some info about your source as well.\n"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)