from fastapi import FastAPI
import requests

app = FastAPI()


def get_pic():
    pic_url = "https://api.btstu.cn/sjbz/api.php?format=json&lx=fengjing"
    r = requests.get(pic_url).json()
    return r["imgurl"]


def send_msg(title, content):
    data = {
        "secret": "vanmay",
        "type": "textcard",
        "title": title,
        "content": content,
    }
    url = "https://wpush-thund1r.vercel.app/send"
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(wecom_url, data=body, headers=headers)


def checkin():
    cookie = '_ga=GA1.2.2103527506.1645192628; _gid=GA1.2.1353685182.1645192628; koa:sess=eyJ1c2VySWQiOjEzNDA4NSwiX2V4cGlyZSI6MTY3MTExMjgwMzA2NSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=kXVPuCq0-U9Ob5IdqoT8ov2mXQg'
    referer = 'https://glados.rocks/console/checkin'
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
    send_msg(title, content)


@app.get('/')
async def index():
    checkin()
    return "<h1>搭建成功</h1>"
