'''------------------------------------------------------------------------------------------------------

#本项目主要用于将漫画网站里的网页代码按顺序下载到本地的网页文件里
#漫画网站：https://www.manhuadb.com/
#漫画网页：https://www.manhuadb.com/manhua/10898/13063_183193.html
#漫画名：苍之瞳的少女
#本地位置为:E:\scrapy_result\苍之瞳

------------------------------------------------------------------------------------------------------'''


#导入相对应的爬虫库(可在urllib或request库二取其一)
from urllib import parse, request
import requests
from bs4 import BeautifulSoup

#本函数功能：在字符串str中查找以head为开头，以end为结尾的语句，并返回从其开头第7位到末尾第4位之间的字母
def catch_infor(str,head,end):
    infor_postion_start = str.find(head)
    infor_postion_end = str.find(end, infor_postion_start+1)
    if infor_postion_start == -1:
        return "none"
    else:
        infor = str[infor_postion_start+2: infor_postion_end]
        # print(type(str))
        #调试时确认是否能返回正确位置值
        # print("start=", infor_postion_start)
        # print("end=", infor_postion_end)
        #print(infor)
        return infor

#输入要爬的网页
url ="https://www.manhuadb.com/manhua/10898/13063_183194.html"
#输入报头信息
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    # 'accept-language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Host': 'i1.manhuadb.com',
    # 'Upgrade-Insecure-Requests': '1'
}

header_final = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    # 'accept-language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'i1.manhuadb.com',
    'Upgrade-Insecure-Requests': '1'
}
proxy = {
    'http': '223.199.24.230:9999'
}
#访问网页并获取信息
# response = requests.get(url, headers=header, proxies=proxy)
response = requests.get(url, headers=header)
page_content = response.content.decode("utf-8")
print(response)
soup = BeautifulSoup(page_content, "html.parser")
# with open('E:\\scrapy_result\\苍之瞳\\text.html','w', encoding='utf-8') as k:
#     k.write(page_content)
li_list = soup.find_all("li")
for k in li_list:
    page_num = catch_infor(str(k), "共", "页")
    if page_num != "none":
        print(page_num)
        break
count = 1
url_list = []
while count <= int(page_num):
    url_img =f"https://www.manhuadb.com/manhua/10898/13063_183194_p{count}.html"
    response_img = requests.get(url_img, headers=header, timeout=10)
    page_content_img = response_img.content.decode("utf-8")
    soup2 = BeautifulSoup(page_content_img, "html.parser")
    #src后面的内容可以直接用节点名来查找
    url_final = soup2.find("img")['src']
    print(url_final)
    # response_final = requests.get(url_final, headers=header_final, timeout=10)
    #保存图片
    # print(response_final)
    # open(f"E:\\scrapy_result\\苍之瞳\\vol_2\\{count}.jpg", "wb").write(response_final.content)
    url_list.append(url_final)
    count += 1
countx = 1
for u in url_list:
    print(f"第{countx}页开工")
    response = requests.get(u, headers=header)
    print(response)
    open(f"E:\scrapy_result\苍之瞳\\vol_2\\{countx}.jpg", "wb").write(response.content)
    print("over")
    countx += 1
print(f"全部{count-1}页下载完毕")

