from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import json
import config
import glados


app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>VercelCheckin</title>
    </head>
    <body>
        <h1>VercelCheckin is running</h1>
        <p>推送类型:<%PUSHTYPE%/></p>
        <p>推送秘钥:<%PUSHTOKEN%/></p>
        <p>GLADOS配置:<%GLADOS%/></p>
        <script>
        </script>
    </body>
</html>
"""


@app.get('/glados')
async def glados():
    return glados.checkin()


@app.get('/')
async def index():
    push_type = config.get("push_type")
    push_token = config.get("push_token")
    glados_cookie = config.get("glados_cookie")
    return HTMLResponse(html.replace('<%PUSHTYPE%/>', push_type).replace('<%PUSHTOKEN%/>', push_token).replace('<%GLADOS%/>', glados_cookie))
