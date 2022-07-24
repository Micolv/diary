from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import requests
import json


app = FastAPI()
index_html = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon"
        href="https://fastly.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.1.1/svgs/regular/calendar-check.svg">
    <title>Diary</title>
</head>

<body>
    <section>
        <div class="container">
            Diary
        </div>
    </section>
</body>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        background: linear-gradient(to bottom right, #0184cf, #77A1D3, #a0eacf);
    }

    .container {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 100px;
    }

    section {
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        min-height: 100vh;
    }
</style>

</html>
"""

show_html = '''
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WPUSH</title>
</head>

<body>
    <div id="app">
        <!-- 显示消息 -->
        <section>
            <div class="container">
                <div class="pic">
                    <span>
                        <img
                            src='<&p&>'>
                        </img>
                    </span>
                </div>
                <h2 class="title">
                    <&t&>
                </h2>
                <h3 class="content">
                    <&c&>
                </h3>
            </div>
        </section>
    </div>
</body>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        background: linear-gradient(to bottom right, #0184cf, #77A1D3, #a0eacf);
    }

    .container {
        width: 90%;
    }

    article {
        padding: 16px;
        background-color: white;
        border-radius: 8px;
        margin-bottom: 16px;
    }

    pre {
        white-space: pre-wrap;
        word-break: break-all;
        margin: 0px;
        font-size: 14px;
    }

    .pic {
        margin: 16px 0;
        padding: 12px;
        background-color: white;
        border-radius: 8px;
    }

    .title {
        margin: 16px 0 6px;
        color: #fff;
    }

    img {
        max-width: 100%;
        max-height: 100%;
    }

    span {
        font-size: 0;
        display: table-cell;
        text-align: center;
        vertical-align: middle;
    }


    .content {
        color: white;
        margin-bottom: 16px;
    }

    section {
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        min-height: 100vh;
    }
    .pic{display:none}
    .title{display:none}
    .content{display:none}
</style>

</html>
'''


@app.get('/')
async def index():
    return HTMLResponse(index_html)


@app.get("/show/")
async def show(p=Query(None), t=Query(None), c=Query(None)):
    html = show_html
    if p != None:
        html = html.replace(".pic{display:none}", "").replace("<&p&>", p)
    if t != None:
        html = html.replace(".title{display:none}", "").replace("<&t&>", t)
    if c != None:
        html = html.replace(".content{display:none}", "").replace("<&c&>", c)
    return HTMLResponse(html)
