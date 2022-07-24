<h1 align="center">Diary</h1>
<h6 align="center">基于 Python Fastapi 部署于 Vercel 的简易图文展示</h6>

## Introduction

- 在地址栏携带参数访问即可实现简易的图文展示
- 用于企业微信机器人多图文推送场景下的链接插入与内容展示
- 当前只支持Get请求，只支持一张图片以及简短的文字内容
- 路径示例:https://XXX.vercel.app/show/?p=XXX&t=XXX&c=XXX

| 参数名 |   含义   | 是否必填 |
| :----: | :------: | :------: |
|   p    | 图片链接 |    否    |
|   t    |   标题   |    否    |
|   c    |   内容   |    否    |
