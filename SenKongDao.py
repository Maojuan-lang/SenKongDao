import json
import os
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

def get_uid_and_atoken():
    account_list = []
    # Github Actions 传递的 secrets
    if "UID" in os.environ and "ATOKEN" in os.environ:
        # 使用环境变量中的 UID 和 ATOKEN
        print("使用环境变量")
        uid_env = os.environ["UID"]
        atoken_env = os.environ["ATOKEN"]
        uids = uid_env.split('\n')
        atokens = atoken_env.split('\n')
        
        # 遍历所有账号
        account_list = [(uid.strip(), atoken.strip()) for uid, atoken in zip(uids, atokens)]
    else:
        cookie_file = open("SenKongDao_config.txt", "r+", encoding="utf8")
        cookie_lines = cookie_file.readlines()
        cookie_file.close()

        # 将文件中的配置存储为元组的列表
        for cookie_line in cookie_lines:
            configs = cookie_line.split("&")
            uid = configs[0].strip()
            atoken = configs[1].strip()
            account_list.append((uid, atoken))

    print("已读取" + str(len(account_list)) + "个cookie")
    print(str(sleep_time) + "秒后进行签到...")
    time.sleep(sleep_time)
    return account_list

# 遍历cookie
account_list = get_uid_and_atoken()
for uid, atoken in account_list:
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
