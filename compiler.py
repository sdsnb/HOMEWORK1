"""输入程序的名字,寻找保留字及其个数
语法检查器？比如检测冒号、括号、空格"""
import keyword
import os
FindPath = r"E:\py\pythonProject\lectureProgject\lecture 1"#存放检测文件的根目录

def main():
    flag = 0
    try:#检测文件名字以及是否存在
        fileName = input("输入想检测的文件名字(xxx.py):\n")
        if fileName.find(".py",0,len(fileName))==-1: #检查是否为py文件
            raise Exception("输入格式错误!")
        FileNames = os.listdir(FindPath)
        for file in FileNames:#遍历当前目录，对比是否有该文件
            name = os.path.join(FindPath,file)
            if (name.find(fileName,0,len(name))!=-1):
                flag = 1
        if flag == 0:
            raise Exception("未找到文件!")
        else:
            catch_Word(str_Processing(fileName))
    except Exception as erro:
        print(erro)


def str_Processing(fileName):#处理文件中的特殊符号
    f = open(r'E:\py\pythonProject\lectureProgject\lecture 1\%s'%fileName, encoding='utf-8')
    data = f.read()
    data = data.lower()
    for i in r'~!@#$%^&*()_+-[]{},.\?':
        data = data.replace(i, " ")
    return data

def catch_Word(strdata):
    words = str(strdata).split()#将每个单词分开
    counts = {}
    for word in words:#如果遇到关键字就使其value+1，字典中没有就创建一个新key
        if keyword.iskeyword(word):
            counts[word] = counts.get(word, 0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    print("---------keywordlist---------")
    for i in range(len(items)):
        key_word, key_count = items[i]
        print("{0:<10}{1:>5}".format(key_word, key_count))
