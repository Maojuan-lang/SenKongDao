import json
import sys
import time
import datetime
import headersGenerator
import requests
import constants

# 常量引入
success_code = constants.success_code
sleep_time = constants.sleep_time
sign_url = constants.sign_url
app_version = constants.app_version

# 打印当前时间
print("当前时间为：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 读取cookie
cookie_file = open("SenKongDao_config.txt", "r+", encoding="utf8")
cookie_lines = cookie_file.readlines()
cookie_file.close()
print("已读取" + str(len(cookie_lines)) + "个cookie")
print(str(sleep_time) + "秒后进行签到...")
time.sleep(sleep_time)

# 遍历cookie
for cookie_line in cookie_lines:
    # 忽略以#开头的行（注释）
    if cookie_line.startswith('#'):
        continue

    # 准备签到信息
    configs = cookie_line.split("&")
    uid = configs[0].strip()
    atoken = configs[1].strip()

    # 获取签到用的值
    cred_resp = headersGenerator.get_cred_by_token(atoken)
    sign_token = cred_resp['token']
    sign_cred = cred_resp['cred']

    # headers初始化
    init_headers = {
        'user-agent': 'Skland/'+app_version+' (com.hypergryph.skland; build:100501001; Android 25; ) Okhttp/4.11.0',
        'cred': sign_cred,
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
    }

    # body
    data = {
        "uid": str(uid),
        "gameId": 1
    }

    # headers添加加密参
    headers = headersGenerator.get_sign_header(sign_url, 'post', data, init_headers, sign_token)

    # 签到请求
    sign_response = requests.post(headers=headers, url=sign_url, json=data)

    # 检验返回是否为json格式
    try:
        sign_response_json = json.loads(sign_response.text)
    except:
        print(sign_response.text)
        print("返回结果非json格式，请检查...")
        time.sleep(sleep_time)
        sys.exit()

    # 如果为json则解析
    code = sign_response_json.get("code")
    message = sign_response_json.get("message")
    data = sign_response_json.get("data")

    # 返回成功的话，打印详细信息
    if code == success_code:
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
    time.sleep(sleep_time)

print("程序运行结束")