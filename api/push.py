from . import config
import json
import requests


def push_msg(title, content):
    pushplus = config.get("pushplus")
    server = config.get("server")
    if pushplus:
        push_url = 'http://www.pushplus.plus/send'
        data = {
            "token": pushplus,
            "template": "markdown",
            "title": title,
            "content": content
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        requests.post(push_url, data=body, headers=headers)
    elif server:
        push_url = "https://sctapi.ftqq.com/{}.send".format(server)
        data = {
            "title": title,
            "desp": content,
        }
        requests.post(push_url, data)
