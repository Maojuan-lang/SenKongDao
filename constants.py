# app信息
app_code = '4ca99fa6b56cc2ba'
app_version = '1.5.1'

# 使用认证代码获得cred
cred_code_url = "https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code"
# 使用token获得认证代码
grant_code_url = "https://as.hypergryph.com/user/oauth2/v2/grant"
# 签到url post请求
sign_url = "https://zonai.skland.com/api/v1/game/attendance"

# 请求成功的code码
success_code = 0
# 休眠x秒继续其他账号签到
sleep_time = 3