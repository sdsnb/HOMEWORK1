#爬一个网页，获取所有的link，然后递归爬这些link里的子link

import requests as req          
from bs4 import BeautifulSoup   

crawded_number = 0              #总共爬过多少链接
except_layer = 5               #想爬多少层
layer = 0                       #记录当前层数的标志

def GetURL():
    url = input("请输入想爬网站(www.xxx.com):")      # 获取输入
    if ("https" or "http") not in url:
        url = str(r"https://" + url)         #获取HTML网页，对应HTTP的GET
    return url

def GetLink(data):
    global crawded_number
    global layer
    global except_layer
    if layer < except_layer:#用于判断当前层数，以防一直递归程序无法中断
        layer += 1
        link_list=[]
        links = req.get(data)
        soup = BeautifulSoup(links.text,"html.parser")       #使用BeautifulSoup解析获取到的数据
        for link in soup.find_all("a"):
            crawded_number+=1
            each_link = link.get("href")
            link_list.append(each_link)
            GetLink(each_link)
        link_print(link_list)
    else:
        return 0
    

def link_print(mylist):
    for i in list(mylist):
        if (r"http://" or r"http://") in str(i):
            print(i)


def main():
    urldata = GetURL()
    GetLink(urldata)

if __name__ == "__main__":
    main()