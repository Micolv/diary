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
        <p>推送配置：<%PUSH%/></p>
        <p>GLADOS配置：<%GLADOS%/></p>
        <script>
        </script>
    </body>
</html>
"""


@app.get('/glados')
async def glados_checkin():
    return glados.checkin()


@app.get('/')
async def index():
    push = bool(config.get("pushplus") or config.get("server"))
    glados = bool(config.get("glados_cookie"))
    return HTMLResponse(html.replace('<%PUSH%/>', push).replace('<%GLADOS%/>', glados))
