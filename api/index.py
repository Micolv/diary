from fastapi import FastAPI
import requests
import os
import json

app = FastAPI()
index_html = '''
<html><body><h1>搭建成功</h1></body></html>
'''


def get_pic():
    pic_url = "https://api.btstu.cn/sjbz/api.php?format=json&lx=fengjing"
    r = requests.get(pic_url).json()
    return r["imgurl"]


def push_msg(title, content):
    data = {
        "secret": "vanmay",
        "type": "textcard",
        "title": title,
        "content": content,
    }
    push_url = "https://wpush-thund1r.vercel.app/send"
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(push_url, data=body, headers=headers)


@app.get('/gla')
async def gla():
    cookie = '_ga=GA1.2.360396571.1652294051; _gid=GA1.2.1042683980.1652294051; koa:sess=eyJ1c2VySWQiOjEzNDA4NSwiX2V4cGlyZSI6MTY3ODIxNDEwODMxMCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=eR4Pv07mpEFifxEjTvJctbH_dHI; _gat_gtag_UA_104464600_2=1'
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
        'token': 'glados_network'
    }
    checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                            'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
    state = requests.get(url2, headers={
                         'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
    if 'message' in checkin.text:
        title = 'GLaDOS签到成功'
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        content = checkin.json()['message'] + '，有效期还剩' + time + '天'
    else:
        title = 'GLaDOS签到失败'
        content = 'Cookie过期'
    push_msg(title, content)


@app.get('/')
async def index():
    return index_html
