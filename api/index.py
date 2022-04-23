# -*- coding: utf8 -*-
import json
import requests

# 企业微信机器人配置
corpid = "ww88c69338045fb2af"
corpsecret = "8OSHUJ1Ct2Bj7Pgl-odb-ediYPKMqRdfX27qCcKIO4k"
agentid = "1000002"

# 获取bing每日壁纸链接


def get_bing():
    bing_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    res = requests.get(bing_url).json()
    bing_pic = "https://cn.bing.com/"+res["images"][0]["url"]
    return bing_pic

# 获取调用接口凭证


def get_token(corpid, corpsecret):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {
        'corpid': corpid,
        'corpsecret': corpsecret,
    }
    req = requests.get(url, params=values)
    data = json.loads(req.text)
    if data["errcode"] == 0:
        return data["access_token"]
    else:
        print("企业微信access_token获取失败: " + str(data))
        return None

# 处理数据


def handle_message(push_data):
    type = "text"
    title = "No Title"
    content = "No Content"
    picurl = get_bing()
    btnurl = picurl
    btninfo = '<a href="'+picurl+'">每日必应图片~</a>'

    if 'type' in push_data and push_data["type"] != "":
        type = push_data["type"]
    if 'title' in push_data and push_data["title"] != "":
        title = push_data["title"]
    if 'content' in push_data and push_data["content"] != "":
        content = push_data["content"]
    if 'picurl' in push_data and push_data["picurl"] != "":
        picurl = push_data["picurl"]
    if 'url' in push_data and push_data["url"] != "":
        btnurl = push_data["url"]
        btninfo = '<a href="'+btnurl+'">点此前往~</a>'

    article = [{
        "title": title,
        "description": content,
        "url": btnurl,
        "picurl": picurl
    }]
    if 'article' in push_data and push_data["article"] != "":
        article = push_data["article"]
    if type == 'text':
        values = {
            "touser": "@all",
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": agentid,
            "text": {
                "content": "【"+title+"】\n"+content+"\n"+btninfo
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
    elif type == 'textcard':
        values = {
            "touser": "@all",
            "toparty": "",
            "totag": "",
            "msgtype": "textcard",
            "agentid": agentid,
            "textcard": {
                "title": title,
                "description": content,
                "url": btnurl,
                "btntxt": "More"
            },
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
    elif type == 'news':
        values = {
            "touser": "@all",
            "toparty": "",
            "totag": "",
            "msgtype": "news",
            "agentid": agentid,
            "news": {
                "articles": article
            },
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }

    return values


# 推送信息


def push(push_data, corpid, corpsecret, agentid):
    values = handle_message(push_data)
    token = get_token(corpid, corpsecret)
    if token is None:
        return
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
    resp = requests.post(url, json=values)
    data = json.loads(resp.text)
    if data["errcode"] == 0:
        return 1
    elif data["errcode"] != 0:
        print("企业微信消息发送失败: "+str(data))
        return 0


def main_handler(event, context):
    http_method = event["httpMethod"]
    if http_method == 'GET':
        push_data = event["queryString"]
    elif http_method == 'POST':
        push_data = json.loads(event["body"])
    res = push(push_data, corpid, corpsecret, agentid)
    if res == 1:
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": "<html><body><h1>Push Success!</h1></body></html>"
        }
    else:
        return {
            "isBase64Encoded": False,
            "statusCode": 404,
            "headers": {"Content-Type": "text/html"},
            "body": "<html><body><h1>Push Fail!</h1><a href='https://console.cloud.tencent.com/scf/list-detail?rid=1&ns=default&id=APITEST&menu=log&tab=codeTab'>Click Here And Check The Log</a></body></html>"
        }
