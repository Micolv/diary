<h1 align="center">Vercel Checkin</h1>
<h6 align="center">基于 Python Fastapi 部署于 Vercel 的签到服务</h6>

## Preparation

- Pushplus推送Token或Server酱SendKey（同时配置优先PUSHPLUS）
- GLADOS登录后cookie值

## Checkin

### GLADOS

- 描述：GLADOS签到领取流量
- 地址：/glados
- 方法：GET

### EVERPHOTO

- 描述：时光相册签到领取空间容量
- 地址：/everphoto
- 方法：GET

### To Be Continue...

## Deployment

- 环境变量

|  环境变量名   |           含义            | 是否必填 |
| :-----------: | :-----------------------: | :------: |
|   PUSHPLUS    |     Pushplus推送Token     |    否    |
|    SERVER     |      Server酱SendKey      |    否    |
| GLADOS_COOKIE |   GLADOS登录后cookie值    |    否    |
|    EPPHONE    | 时光相册手机号（默认+86） |    否    |
|     EPPWD     |       时光相册密码        |    否    |

- 建议右键点击下方按钮新页面打开链接完成部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FThund1R%2Fvercel-checkin&env=PUSHPLUS,SERVER,GLADOS_COOKIE&envDescription=%E4%B8%8D%E9%85%8D%E7%BD%AE%E8%BE%93%E5%85%A5%E7%A9%BA%E6%A0%BC%E5%8D%B3%E5%8F%AF%EF%BC%8C%E5%A1%AB%E5%86%99%E8%AF%A6%E6%83%85%E8%AF%B7%E7%82%B9%E5%87%BB%E5%8F%B3%E4%BE%A7%E2%86%92_%E2%86%92&envLink=https%3A%2F%2Fgithub.com%2FThund1R%2Fvercel-checkin%23deployment)
