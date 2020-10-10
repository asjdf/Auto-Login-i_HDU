import requests

userName = 20333322
# 学号
pwd = 22222222
# 登录密码

# 登录
data = {'opr' : 'pwdLogin',
        'userName' : userName,
        'pwd' : pwd,
        'rememberPwd' : '0'
        }
r = requests.post('http://2.2.2.2/ac_portal/login.php',data)
print(r.content)

# 登出
# data = {'opr' : 'logout'}
# r = requests.post('http://2.2.2.2/ac_portal/login.php',data1)
# print(r.content.decode('utf-8'))