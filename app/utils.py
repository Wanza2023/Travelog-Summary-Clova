import json
import httpx
import re
import constant

def clova_api(title, content):
    r = httpx.post(
        'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize',
        json ={
            "document": {
                "title": title,
                "content": content,
            },
            "option": {
                "language": "ko",
                "model": "general",
                "tone": 0,
                "summaryCount": 3
            }
        },
        headers = {
            'Content-Type': 'application/json;UTF-8',
            'X-NCP-APIGW-API-KEY-ID': constant.client_id,
            'X-NCP-APIGW-API-KEY': constant.client_secret
        }
    )

    return json.loads(r.text)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  cleantext = ' '.join(cleantext.split())
  return cleantext