from fastapi import FastAPI
import requests

app = FastAPI()


def get_bing():
    bing_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    res = requests.get(bing_url).json()
    bing_pic = "https://cn.bing.com/"+res["images"][0]["url"]
    return bing_pic


@app.get('/')
async def hello():
    res = get_bing()
    return {'message': res}
