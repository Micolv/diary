# -*- coding: utf8 -*-
import json
import requests
from http.server import BaseHTTPRequestHandler
import datetime
import re

# 推送API网关地址
wecon_url = "https://service-2rtviz4c-1258742711.gz.apigw.tencentcs.com/release/WecomRobot"

# 获取词霸图片与每日一句


def get_ciba():
    ciba_url = "http://open.iciba.com/dsapi/"
    r = requests.get(ciba_url)
    r = json.loads(r.text)
    content = r["content"]
    note = r["note"]
    ciba_share = r["fenxiang_img"]
    ciba_pic = r["picture3"]
    ciba_sentence = content + "\n" + note
    return {
        "ciba_sentence": ciba_sentence,
        "ciba_share": ciba_share,
        "ciba_pic": ciba_pic
    }


# 推送信息


def push_message():
    ciba_data = get_ciba()
    ciba_sentence = ciba_data["ciba_sentence"]
    ciba_share = ciba_data["ciba_share"]

    data = {
        "type": "news",
        "title": ciba_sentence,
        "url": ciba_share,
        "picurl": ciba_share
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(wecon_url, data=body, headers=headers)


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        push_message()
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        return