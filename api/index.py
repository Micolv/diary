# -*- coding: utf8 -*-
import json
import requests
from http.server import BaseHTTPRequestHandler
import datetime
import re

# 推送API网关地址
wecon_url = "https://service-2rtviz4c-1258742711.gz.apigw.tencentcs.com/release/WecomRobot"
# 和风天气key
qweather_key = '533885fb5b4f42dcbaf709ae76f59c2f'
# 天气预报地址
city = "南充"
county = "蓬安"

# 获取当前日期


def get_date():
    a = datetime.datetime.now()
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)
    date = y + '年' + m + '月' + d + '日'
    return date

# 获取随机图片


def get_pic():
    pic_url = "https://api.btstu.cn/sjbz/api.php?format=json&lx=fengjing"
    r = requests.get(pic_url).json()
    return r["imgurl"]

# 获取bing每日壁纸链接


def get_bing():
    bing_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    res = requests.get(bing_url).json()
    bing_pic = "https://cn.bing.com/"+res["images"][0]["url"]
    bing_title = res["images"][0]["copyright"]
    bing_title = re.sub(u"\\(.*?\\)", "", bing_title)
    return {
        "bing_pic": bing_pic,
        "bing_title": bing_title
    }

# 获取城市ID


def get_city_id():
    city_url = f'https://geoapi.qweather.com/v2/city/lookup?key={qweather_key}&location={city}'
    city_json = requests.get(city_url).json()
    city_code = city_json["code"]
    if city_code.__eq__("200"):
        for city_data in city_json["location"]:
            city_name = city_data["name"]
            if city_name.__eq__(county):
                city_id = city_data["id"]
                return city_id

    else:
        print("访问获取地区接口失败！")
        return "访问获取地区接口失败！"

# 获取城市天气信息


def get_today_weater():
    city_id = get_city_id()
    weather_url = f"https://devapi.qweather.com/v7/weather/3d?key={qweather_key}&location={city_id}"
    weather_json = requests.get(weather_url).json()
    weather_link = weather_json["fxLink"]
    res_code = weather_json["code"]
    if res_code.__eq__("200"):
        today_weather = weather_json["daily"][0]
        weather_info = f"{today_weather['textDay']}，{today_weather['tempMin']}~{today_weather['tempMax']}℃"
        return {
            'weather_info': weather_info,
            'weather_link': weather_link
        }

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
    today_date = get_date()
    bing_data = get_bing()
    weather_data = get_today_weater()
    bing_pic = bing_data["bing_pic"]
    bing_title = bing_data["bing_title"]
    ciba_data = get_ciba()
    ciba_sentence = ciba_data["ciba_sentence"]
    ciba_share = ciba_data["ciba_share"]
    weather_info = weather_data["weather_info"]
    weather_link = weather_data["weather_link"]

    data = {
        "type": "news",
        "article": [{
            "title": today_date+"\n"+bing_title,
            "url": bing_pic,
            "picurl": bing_pic
        }, {
            "title": ciba_sentence,
            "url": ciba_share,
            "picurl": ciba_share
        }, {
            "title": "今天天气："+weather_info,
            "url": weather_link,
            "picurl": get_pic()
        }, {
            "title": "JD Sign In",
            "url": "https://signfree.jd.com/?activityId=PiuLvM8vamONsWzC0wqBGQ",
            "picurl": get_pic()
        }]
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(wecon_url, data=body, headers=headers)


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.push_message()
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        with open(join('data', 'file.txt'), 'r') as file:
          for line in file:
            self.wfile.write(line.encode())
        return