from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import json
from . import config, glados, everphoto


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
        <p>推送配置：<%PUSH%/></p>
        <p>GLADOS配置：<%GLADOS%/></p>
        <p>时光相册配置：<%EVERPHOTO%/></p>
        <script>
        </script>
    </body>
</html>
"""


@app.get('/glados')
async def glados_checkin():
    return glados.checkin()


@app.get('/everphoto')
async def everphoto_checkin():
    return everphoto.checkin()


@app.get('/')
async def index():
    push = str(bool(config.get("pushplus") or config.get("server")))
    glados = str(bool(config.get("glados_cookie")))
    everphoto = str(bool(config.get("epphone") and config.get("eppwd")))
    return HTMLResponse(html.replace('<%PUSH%/>', push).replace('<%GLADOS%/>', glados).replace('<%EVERPHOTO%/>', everphoto))
