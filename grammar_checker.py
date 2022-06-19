'''自动检测代码语法错误并提示？'''
import os
filepath = r"D:\pythonjiance"#存放检测文件的根目录

def StrP(fileName):#逐行打开文件
    a = open(r'D:\pythonjiance\%s'%fileName, encoding='utf-8')
    data = a.readlines()
    return data

def c_error(strdata):
    b =0#记录错误数
    for eachline in strdata:
        left=right=0#记录括号数
        colon=0#记录冒号数
        keywords=0
        temp=str(eachline).lower()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            data = temp.replace(i, " ")
        data = data.split()
        for word in data:
            if word in ["try","def","if","elif","else","except","for","while"]:
                keywords=keywords+1#检测需要冒号的关键字
        for eachword in eachline:#左括号和右括号，函数与冒号一一对应
            if eachword == "(":
                left=left+1
            if eachword == ")":
                right=right+1
            if eachword == ":" and keywords!=0:
                colon+=1

        if left != right:
            print("%s----->此处缺少括号"%eachline)
            b=b+1
        elif colon != keywords:
            print("%s----->此处缺少冒号"%eachline)
            b=b+1
    if b != 0:   
        print("发现%s个错误"%b)
    else:
        print("未发现错误")

def main():
    flag = 0
    try:#检测文件名字以及是否存在
        fileName = input("输入想检测的文件名字(xxx.py):\n")
        if fileName.find(".py",0,len(fileName))==-1: #检查是否为py文件
            raise Exception("输入格式错误!")
        FileNames = os.listdir(filepath)
        for file in FileNames:#遍历当前目录，对比是否有该文件
            name = os.path.join(filepath,file)
            if (name.find(fileName,0,len(name))!=-1):
                flag = 1
        if flag == 0:
            raise Exception("未找到文件!")
        else:
            c_error(StrP(fileName))
    except Exception as erro:
        print(erro)

