from . import config, push
import requests
import json
import hashlib

epphone = config.get("epphone")
eppwd = config.get("eppwd")
header = {
    "User-Agent": "EverPhoto/2.7.0 (Android;2702;ONEPLUS A6000;28;oppo)",
    "x-device-mac": "02:00:00:00:00:00",
    "application": "tc.everphoto",
    "authorization": "Bearer 94P6RfZFfqvVQ2hH4jULaYGI",
    "x-locked": "1",
    "content-length": "0",
    "accept-encoding": "gzip"
}


def get_pwd_md5(eppwd):
    salt = "tc.everphoto."
    pwd = salt + eppwd
    md5 = hashlib.md5(pwd.encode())
    return md5.hexdigest()


def login():
    login_url = "https://web.everphoto.cn/api/auth"
    pwd = get_pwd_md5(eppwd)
    phone = epphone if epphone[0] == "+" else "+86" + epphone
    data = {
        "mobile": phone,
        "password": pwd
    }
    res = requests.post(login_url, data=data, headers=header).json()
    return res


def checkin():
    if epphone and eppwd:
        try:
            log = login()
            check_url = "https://api.everphoto.cn/users/self/checkin/v2"
            header["authorization"] = "Bearer "+log["data"]["token"]
            res = requests.post(check_url, headers=header).json()
            name = log["data"]["user_profile"]["name"]
            tomorrowReward = res["data"]["tomorrow_reward"]/1024/1024
            totalReward = res["data"]["total_reward"]/1024/1024/1024
            if res["data"]["checkin_result"] == True:
                title = "时光相册签到成功"
                todayReward = res["data"]["reward"]/1024/1024
                content = "账号："+name+"\n\n今日获得："+str(todayReward)+"M\n\n明日可得："+str(tomorrowReward) + \
                    "M\n\n总共获得："+str(round(totalReward, 2))+"G。\n\n - - - "
            else:
                title = "时光相册签到重复"
                content = "账号："+name+"\n\n明日可得："+str(tomorrowReward) + \
                    "M\n\n总共获得："+str(round(totalReward, 2))+"G。\n\n - - - "
            code = 200
        except Exception as errorMsg:
            print("时光相册签到异常", errorMsg)
            title = "时光相册签到异常，" + repr(errorMsg)
            content = "异常信息：" + repr(errorMsg) + "，请检查控制台报错信息。\n\n - - - "
            code = 500
    else:
        title = "时光相册配置缺失，请在Vercel环境变量中配置EPPHONE和EPPWD"
        content = "请在Vercel环境变量中配置EPPHONE和EPPWD"
        code = 401
    push.push_msg(title, content)
    return {"code": code, "msg": title}
