from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import json
from . import config, glados


app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="icon" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.1.1/svgs/regular/calendar-check.svg">
        <title>VercelCheckin</title>
    </head>
    <body>
        <h1>VercelCheckin is running</h1>
        <p>配置状态：</p>
        <p>推送类型：<%PUSHTYPE%/></p>
        <p>推送秘钥：<%PUSHTOKEN%/></p>
        <p>GLADOS配置：<%GLADOS%/></p>
        <script>
        </script>
    </body>
</html>
"""


def verify_params(item):
    res = config.get(item)
    if res:
        return "有"
    else:
        return "无"


@app.get('/glados')
async def glados_checkin():
    return glados.checkin()


@app.get('/')
async def index():
    push_type = verify_params("push_type")
    push_token = verify_params("push_token")
    glados_cookie = verify_params("glados_cookie")
    return HTMLResponse(html.replace('<%PUSHTYPE%/>', push_type).replace('<%PUSHTOKEN%/>', push_token).replace('<%GLADOS%/>', glados_cookie))
