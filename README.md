<h1 align="center">Vercel Checkin</h1>
<h6 align="center">基于 Python Fastapi 部署于 Vercel 的签到服务</h6>

## Preparation

- Pushplus推送Token或Server酱SendKey
- GLADOS登录后cookie值

## Checkin

### GLADOS

- 描述：GLADOS签到领取流量
- 地址：/glados
- 方法：GET

## Deployment

- 环境变量

|  环境变量名   |                     含义                     | 是否必填 |
| :-----------: | :------------------------------------------: | :------: |
|   PUSH_TYPE   |    推送类型，填1为Pushplus，填2为Server酱    |    是    |
|  PUSH_TOKEN   | 推送秘钥，Pushplus推送Token或Server酱SendKey |    是    |
| GLADOS_COOKIE |             GLADOS登录后cookie值             |    否    |

- 建议右键点击下方按钮新页面打开链接完成部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FThund1R%2Fvercel-checkin&env=PUSH_TYPE,PUSH_TOKEN&envDescription=%E8%AF%A6%E6%83%85%E8%AF%B7%E7%82%B9%E5%87%BB%E5%8F%B3%E4%BE%A7%E2%86%92_%E2%86%92&envLink=https%3A%2F%2Fgithub.com%2FThund1R%2Fvercel-checkin%23Deployment)
