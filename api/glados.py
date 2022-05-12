from * import config
import json
import requests


def checkin():
    if config.get("glados_cookie"):
        cookie = '_ga=GA1.2.360396571.1652294051; _gid=GA1.2.1042683980.1652294051; koa:sess=eyJ1c2VySWQiOjEzNDA4NSwiX2V4cGlyZSI6MTY3ODIxNDEwODMxMCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=eR4Pv07mpEFifxEjTvJctbH_dHI; _gat_gtag_UA_104464600_2=1'
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
