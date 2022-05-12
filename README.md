<h1 align="center">Vercel Checkin</h1>
<h6 align="center">基于 Python Fastapi 部署于 Vercel 的签到服务</h6>

## 准备

- Pushplus推送Token或Server酱SendKey
- GLADOS登录后cookie值

## 签到

### GLADOS

- 描述：GLADOS签到领取流量
- 地址：/glados
- 方法：GET

## 部署

- 环境变量

|  环境变量名   |                含义                | 是否必填 |
| :-----------: | :--------------------------------: | :------: |
|   PUSH_TYPE   |    填1为Pushplus，填2为Server酱    |    是    |
|  PUSH_TOKEN   | Pushplus推送Token或Server酱SendKey |    是    |
| GLADOS_COOKIE |        GLADOS登录后cookie值        |    否    |

- 建议右键点击下方按钮新页面打开链接完成部署



