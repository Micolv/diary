from . import config,push
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
            title = 'GLaDOS签到成功'
            time = state.json()['data']['leftDays']
            time = time.split('.')[0]
            content = checkin.json()['message'] + '，有效期还剩' + time + '天'
        else:
            title = 'GLaDOS签到失败'
            content = 'Cookie过期'
        msg = title+","+content
        push.push_msg(title, content)
        return {"code": 200, "msg": msg}
    else:
        return {"code": 403, "msg": "请在环境变量中配置GLADOS_COOKIE"}
