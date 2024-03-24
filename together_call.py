import requests, json
import re, os
from dotenv import load_dotenv

_ = load_dotenv()
content = {'id': '8673e10c9a9e5f42-SIN', 'object': 'chat.completion', 'created': 1710918594, 'model': 'mistralai/Mistral-7B-Instruct-v0.2', 'prompt': [], 'choices': [{'finish_reason': 'eos', 'logprobs': None, 'index': 0, 'message': {'role': 'assistant', 'content': ' I have conducted research on Wenzhou Success Group Bags Co. Ltd and Litai (Quanzhou) Bags Corp., Ltd based on publicly available information. However, please note that the accuracy of this information cannot be guaranteed as it is subject to change and may not be complete.\n\n```json\n{\n  "Wenzhou Success Group Bags Co. Ltd": {\n    "Years in Business": "Established in 1993",\n    "user review": "Generally positive reviews on platforms like Alibaba and Made-in-China, with comments praising their product quality and customer service.",\n    "location": "Wenzhou, Zhejiang Province, China",\n    "delivery time": "Typically within 15-30 days, but can be negotiated based on order size and urgency.",\n    "unit": "Minimum order quantity is usually 500 pieces per design.",\n    "logistics (managed by)": "They offer various logistics solutions including DHL, FedEx, and TNT. Clients are responsible for freight charges."\n  },\n  "Litai (Quanzhou) Bags Corp., Ltd": {\n    "Years in Business": "Established in 1995",\n    "user review": "Positive reviews on platforms like Alibaba and Made-in-China, with comments highlighting their competitive pricing and on-time delivery.",\n    "location": "Quanzhou, Fujian Province, China",\n    "delivery time": "Average delivery time is around 30 days, but can be expedited for an additional fee.",\n    "unit": "Minimum order quantity is typically 1,000 pieces per design.",\n    "logistics (managed by)": "They work with multiple logistics providers, allowing clients to choose the most suitable option for their needs."\n  }\n}\n\nSources:\n- Company websites\n- Alibaba\n- Made-in-China\n```'}}], 'usage': {'prompt_tokens': 102, 'completion_tokens': 451, 'total_tokens': 553}}

def together_call(vendor1, vendor2):
    endpoint = 'https://api.together.xyz/v1/chat/completions'
    res = requests.post(endpoint, json={
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "max_tokens": 512,
        "prompt": f'[INST] Provide me information about {vendor1} and {vendor2} vendor in the following json format, for years in business look for keywords like "established, founded etc.":'+' {"Years in Business": ,"user review (star rating)":, "location": , "delivery time":, "unit (how many)": , "logistics (managed by)": , "sources":,} Only search on "https://www.globalsources.com/" to get the information needed. Only return the json in response no extra texts, and keep the keys as it is.[/INST]',
        "temperature": 0,
        "top_p": 0.9,
        "top_k": 10,
        "repetition_penalty": 1,
        "stop": [
            "[/INST]",
            "</s>"
        ],
        "repetitive_penalty": 1,
        "update_at": "2024-03-20T06:25:03.217Z"
    }, headers={
        "Authorization": f"Bearer {os.environ['TOGETHER_API_KEY']}",
    })

    res_dict = json.loads(res.content)
    # res_dict = content
    # print(res_dict)
    if len(res_dict["choices"][0]["message"]["content"].split("```"))>=3:
        sources = res_dict["choices"][0]["message"]["content"].split("```")[2]
    else:
        sources = ""
    # try:
    #     json_string =  json.loads(res_dict["choices"][0]["message"]["content"].split("{")[1])
    #     final_dict =  json.loads(json_string.split("}")[0])
    # except:
    print(res_dict["choices"][0]["message"]["content"])
    print("in except")
    final_dict = json.loads(res_dict["choices"][0]["message"]["content"])

    vendor1_key = vendor1.replace(".",'')
    vendor2_key = vendor2.replace(".",'')
    return ([
    {
        'feature': 'Years in Business',
        vendor1_key: final_dict[vendor1]['Years in Business'],
        vendor2_key: final_dict[vendor2]['Years in Business'],
    },
    {
        'feature': 'Review',
        vendor1_key: final_dict[vendor1]['user review (star rating)'],
        vendor2_key: final_dict[vendor2]['user review (star rating)']
    },
    {
        'feature': 'Delivery Time',
        vendor1_key: final_dict[vendor1]['delivery time'],
        vendor2_key: final_dict[vendor2]['delivery time']
    },
    {
        'feature': 'Location',
        vendor1_key: final_dict[vendor1]['location'],
        vendor2_key: final_dict[vendor2]['location']
    },
    {
        'feature': 'Logistics (Managed by)',
        vendor1_key: final_dict[vendor1]['logistics'],
        vendor2_key: final_dict[vendor2]['logistics']
    },
    {
        'feature': 'Scalability',
        vendor1_key: final_dict[vendor1]['unit'],
        vendor2_key: final_dict[vendor2]['unit']
    }
    # Add more data objects as needed
], sources)

# ,
#     {
#         'feature': 'Customer Support',
#         'vendor1': 'Yes',
#         'vendor2': 'Yes',
    # }
# together_call("Wenzhou Success Group Bags Co. Ltd", "Litai (Quanzhou) Bags Corp., Ltd")