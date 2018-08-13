

###############################################################3333

# # 爬取免费ip
# import time
# from pyquery import PyQuery as pq
# import requests
# import json
#
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}
#
# def parge_item(html):
#     doc = pq(html.text)
#     items = doc("tr").items()
#
#     flag = 0
#     ips = []
#     for item in items:
#         flag += 1
#         if flag == 1:
#             continue
#         tds = item.find("td")
#         ip, port, types = tds[1].text, int(tds[2].text), tds[5].text
#
#         ips.append({'ip': ip, 'port': port, 'type': types})
#     return ips
#
# def check_ip(ips):
#     url = 'https://www.ipip.net/'
#     valid_ip = []
#     for ip in ips:
#         try:
#             proxies = {
#                 'http':ip['ip']
#             }
#             res = requests.get(url, proxies=proxies, headers=header, timeout=2)
#             res.raise_for_status()
#         except:
#             print("invalid ip:", ip[ip])
#         else:
#
#             valid_ip.append(ip)
#     return valid_ip
#
#
# def save_file(ips):
#     with open("ips.json", 'a', encoding='utf-8') as file:
#          file.write(json.dumps(ips, indent=4, ensure_ascii=False))
#
# def get_ip_list(index):
#     url = "http://www.xicidaili.com/nt/{index}".format(index=index)
#
#     try:
#         html = requests.get(url=url, headers=header)
#         html.encoding = html.apparent_encoding
#         html.raise_for_status()
#         results = parge_item(html)
#         # results = check_ip(results)
#         save_file(ips=results)
#
#
#     except Exception as e:
#         print('error', e)
#
# if __name__ == '__main__':
# #     for i in range(1, 11):
# #         get_ip_list(i)
#     get_ip_list(1)
######
#############################################################

# 使用ip代理池
import requests
import random
import json

if __name__ == '__main__':
    with open("ips.json", 'r+', encoding='utf-8') as file:
        res = file.read()
        ip_list = json.loads(res)

    url = "https://www.baidu.com"
    proxies_ip = random.choice(ip_list)
    proxies = {'http': proxies_ip}
    try:
        print(proxies)
        html = requests.get(url, proxies=proxies)
        html.raise_for_status()
        print(html.request)
        html.encoding = html.apparent_encoding
    except Exception as e:
        print(e)
    else:
        print(html.text)


########################################################################################################################

# 测试服务器pymongoDB

# import pymongo
#
# if __name__ == '__main__':
#     client = pymongo.MongoClient(host='localhost',port=27017)
#
#     db = client['servers_test']
#     table = db['hah']
#     data = {
#         'id':'123',
#         'name':'Tom',
#         'age':23
#     }
#     try:
#         if table.insert_one(data):
#             print("save successd!")
#     except Exception as e:
#         print("save failed!")
#         print(e)


########################################################################################################################

# c而是服务器无显示页面的chrome浏览引擎


# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
# wd = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/ubuntu/Chrome/chromedriver')
#
# wd.get("https://www.163.com")
#
# content = wd.page_source.encode('utf-8')
# print(content)
#
# wd.close()
# wd.quit()
