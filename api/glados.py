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
        checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                                'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
        state = requests.get(url2, headers={
            'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
        if 'message' in checkin.text:
            email = state.json()['data']['email']
            time = state.json()['data']['leftDays'].split('.')[0]
            message = checkin.json()['message']
            title = 'GLaDOS签到情况：' + \
                checkin.json()['message'] + '，有效期还剩' + time + '天'
            content = "· 账号：" + email + "\n· 剩余天数："+time+"天\n· 签到信息：" + message
        else:
            title = 'GLaDOS签到失败，请更新Cookie'
            content = 'Cookie过期，请更新'
        push.push_msg(title, content)
        return {"code": 200, "msg": title}
    else:
        return {"code": 403, "msg": "请在Vercel环境变量中配置GLADOS_COOKIE"}
