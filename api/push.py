from . import config
import json
import requests


def push_msg(title, content):
    push_type = config.get("push_type")
    push_token = config.get("push_token")
    if(push_type == "1"):
        push_url = 'http://www.pushplus.plus/send'
        data = {
            "token": push_token,
            "template": "markdown",
            "title": title,
            "content": content
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        requests.post(push_url, data=body, headers=headers)
    elif(push_type == "2"):
        push_url = "https://sctapi.ftqq.com/{}.send".format(push_token)
        data = {
            "title": title,
            "desp": content,
        }
        requests.post(push_url, data)
