# 所有配置项环境变量优先级大于本文件，若配置了环境变量将忽略此文件的配置(注意：vercel 修改环境变量后需要重新部署)！

import os
SYS_CONFIG = {
    # 推送类型，1为pushplus，2为server酱
    "push_type": "",
    # 推送秘钥
    "push_token": ""
}


def get(key: str):
    value = os.getenv(key.upper())
    if value is None:
        key = key.lower()
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value
