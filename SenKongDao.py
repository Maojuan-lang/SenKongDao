import json
import sys
import time
import datetime

import requests

# 声明常量
# 签到url post请求
SIGN_URL = "https://zonai.skland.com/api/v1/game/attendance"
SUCCESS_CODE = 0
# 休眠三秒继续其他账号签到
SLEEP_TIME = 3

# 打印当前时间
print("当前时间为：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 读取cookie
cookie_file = open("SenKongDao_config.txt", "r+", encoding="utf8")
cookie_lines = cookie_file.readlines()
cookie_file.close()
print("已读取" + str(len(cookie_lines)) + "个cookie")
print(str(SLEEP_TIME) + "秒后进行签到...")
time.sleep(SLEEP_TIME)

# 遍历cookie
for cookie_line in cookie_lines:

    # 准备签到信息
    configs = cookie_line.split("&")
    uid = configs[0].strip()
    signing_cookie = configs[1].strip()
    headers = {
        "user-agent": "Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 33; ) Okhttp/4.11.0",
        "cred": signing_cookie,
        "vName": "1.0.1",
        "vCode": "100001014",
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        "dId": "de9759a5afaa634f",
        "platform": "1"
    }
    data = {
        "uid": str(uid),
        "gameId": 1
    }

    # 签到请求
    sign_response = requests.post(headers=headers, url=SIGN_URL, data=data)

    # 检验返回是否为json格式
    try:
        sign_response_json = json.loads(sign_response.text)
    except:
        print(sign_response.text)
        print("返回结果非json格式，请检查...")
        time.sleep(SLEEP_TIME)
        sys.exit()

    # 如果为json则解析
    code = sign_response_json.get("code")
    message = sign_response_json.get("message")
    data = sign_response_json.get("data")

    # 返回成功的话，打印详细信息
    if code == SUCCESS_CODE:
        print("签到成功")
        awards = sign_response_json.get("data").get("awards")
        for award in awards:
            print("签到获得的奖励ID为：" + award.get("resource").get("id"))
            print("此次签到获得了" + str(award.get("count")) + "单位的" + award.get("resource").get("name") + "(" + award.get(
                "resource").get("type") + ")")
            print("奖励类型为：" + award.get("type"))
    else:
        print(sign_response_json)
        print("签到失败，请检查以上信息...")

    # 休眠指定时间后，继续下个账户
    time.sleep(SLEEP_TIME)

print("程序运行结束")
