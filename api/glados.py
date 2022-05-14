from . import config, push
import json
import requests


def checkin():
    if config.get("glados_cookie"):
        cookie = config.get("glados_cookie")
        url = "https://glados.rocks/api/user/checkin"
        url2 = "https://glados.rocks/api/user/status"
        origin = "https://glados.rocks"
        referer = "https://glados.rocks/console/checkin"
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        payload = {
            'token': 'glados.network'
        }
        try:
            checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                                    'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload)).json()
            state = requests.get(url2, headers={
                'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent}).json()
            if checkin['code'] == 0 or checkin['code'] == 1:
                email = state['data']['email']
                time = state['data']['leftDays'].split('.')[0]
                message = checkin['message']
                title = "Glados签到成功，" + message
                content = "账号：" + email + "\n\n剩余天数："+time + \
                    "天\n\n签到信息：" + message + "\n\n - - - "
                push_msg(title, content)
                return {"code": 200, "msg": title}
            else:
                message = checkin['message']
                title = "Glados签到失败，" + message
                content = "错误信息：" + message + "\n\n - - - "
        except Exception as errorMsg:
            print("Glados签到异常:", errorMsg)
            title = "Glados签到异常" + errorMsg
            content = "异常信息：" + errorMsg + "\n\n - - - "
        push_msg(title, content)
        return {"code": 200, "msg": title}
    else:
        return {"code": 403, "msg": "请在Vercel环境变量中配置GLADOS_COOKIE"}
