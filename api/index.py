from fastapi import FastAPI
import requests

app = FastAPI()


def get_pic():
    pic_url = "https://api.btstu.cn/sjbz/api.php?format=json&lx=fengjing"
    r = requests.get(pic_url).json()
    return r["imgurl"]


@app.get('/')
async def hello():
    res = get_pic()
    return {'message': res}
