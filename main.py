import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True, encoding='utf-8')

class i_HDU(object):
    def __init__(self,_userName,_pwd,_tryTimeMax = 5):
        self.userName = _userName
        self.pwd = _pwd
        self.tryTimeMax = _tryTimeMax
    # 登录
    def login(self,tryTime):
        print('正在登录')
        try:
            data = {'opr' : 'pwdLogin',
                    'userName' : self.userName,
                    'pwd' : self.pwd,
                    'rememberPwd' : '0'
                    }
            r = requests.post('http://2.2.2.2/ac_portal/login.php',data,proxies='')
            print(r.content)
            return 0
            pass
        except:
            print('第'+ str(tryTime) +'登录失败，请检查网络连接')
            if tryTime < self.tryTimeMax:
                print('即将开始重试\n')
                return self.login(tryTime+1)
            elif tryTime >= self.tryTimeMax:
                print("超过最大重试次数， 不再尝试")
                return 1
            pass

    # 登出
    def logout(self,tryTime):
        print('正在登出')
        try:
            data = {'opr' : 'logout'}
            r = requests.post('http://2.2.2.2/ac_portal/login.php',data,proxies='')
            print(r.content.decode('utf-8'))
            return 0
            pass
        except:
            print('第'+ str(tryTime) +'登出失败，请检查网络连接')
            if tryTime < self.tryTimeMax:
                print('即将开始重试\n')
                return self.logout(tryTime+1)
            elif tryTime >= self.tryTimeMax:
                print("超过最大重试次数， 不再尝试")
                return 1
            pass

def main():
    print('欢迎使用i_HDU登录助手 By asjdf')
    # 学号
    userName = os.getenv('userName')
    print(userName)
    # 登录密码
    pwd = os.getenv('pwd')
    print(pwd)
    i = i_HDU(userName, pwd)
    i.login(1)
    print('程序结束,再见')
    return 0

if __name__ == '__main__':
    main()