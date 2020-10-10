import requests

userName = 20333322
# 学号
pwd = 22222222
# 登录密码

class i_HDU(object):
    def __init__(self,_userName,_pwd,_tryTimeMax = 5):
        self.userName = _userName
        self.pwd = _pwd
        self.tryTimeMax = _tryTimeMax
    # 登录
    def login(self):
        tryTime = 1
        try:
            data = {'opr' : 'pwdLogin',
                    'userName' : self.userName,
                    'pwd' : self.pwd,
                    'rememberPwd' : '0'
                    }
            r = requests.post('http://2.2.2.2/ac_portal/login.php',data)
            print(r.content)
            return 0
            pass
        except:
            print('第'+ str(tryTime) +'登录失败，请检查网络连接')
            if tryTime <= self.tryTimeMax:
                return self.login(tryTime+1)
            elif tryTime > self.tryTimeMax:
                print("超过最大重试次数， 不再尝试")
            pass


    # 登出
    def logout(self):
        tryTime = 1
        try:
            data = {'opr' : 'logout'}
            r = requests.post('http://2.2.2.2/ac_portal/login.php',data)
            print(r.content.decode('utf-8'))
            return 0
            pass
        except:
            print('第'+ str(tryTime) +'登出失败，请检查网络连接')
            if tryTime <= self.tryTimeMax:
                return self.logout(tryTime+1)
            elif tryTime > self.tryTimeMax:
                print("超过最大重试次数， 不再尝试")
            pass


if __name__ == '__main__':
    i = i_HDU(userName, pwd)
    i.login()