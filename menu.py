import digital_display
import Hash_Function
import big
import proceeding
import compiler
import grammar_checker
import pach
import competition
Manu_Number = 8     #功能数目


def main():
    try:
        menu()
    except Exception as err:
        print(err)#输出raise中的错误类型
        main()


def menu():         #选择主菜单
    print("------------菜单------------")
    option = eval(input("1.七段数码管显示\n2.哈希函数\n3.绘制‘大’字\n4.进度条\n5.编译器检查关键字\n6.语法错误检测\n7.爬虫\n8.模拟比赛\n9.退出\n请选择:"))
    if option <= Manu_Number and option!=0:
        try:
            nextmenu(option)    #如果输入数字满足要求调用子菜单界面
        except Exception as erro:
            print(erro)
            menu()
    elif option == 8:
        return 0
    else:
        raise Exception('请选择菜单内数字！')#对每一次输入都会有判断


def nextmenu(op):#子菜单界面，根据不同的输入参数调用不同的子菜单与功能函数
    if op == 1:
        idx = eval(input('\n------------菜单一------------\n1.显示输入数字\n2.显示输入时间\n3.显示当前时间\n4.返回\n请选择:'))
        if idx <=3 and idx!=0:
            digital_display.main(idx)
            turtle.Turtle._screen = None  #彻底关闭turtle画布，为下次的调用做准备
            turtle.TurtleScreen._RUNNING = True
            nextmenu(op)
        elif idx ==4:
            menu()      #嵌套调用，返回上级菜单
        else:
            raise Exception('请选择菜单内数字！')
        
    elif op ==2:
        idx = eval(input('\n------------菜单二------------\n1.加密字符串\n2.返回主菜单\n请选择:'))
        if idx == 1:
            Hash_Function.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('输入错误，请输入提供的数字选项')
    
    elif op == 3:
        idx = eval(input('\n------------菜单三------------\n1.选择字号及颜色\n2.返回主菜单\n请选择:'))
        if idx == 1:
            big.init()
            turtle.Turtle._screen = None
            turtle.TurtleScreen._RUNNING = True
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字！')

    elif op == 4:
        idx = eval(input('\n------------菜单四------------\n1.展示进度条\n2.返回主菜单\n请选择:'))
        if idx == 1:
            proceeding.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字！')
    
    elif op == 5:
        idx = eval(input('\n------------菜单五------------\n1.检测关键字\n2.返回主菜单\n请选择:'))
        if idx == 1:
            compiler.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字！')

    elif op == 6:
        idx = eval(input('\n------------菜单六------------\n1.输入文件名称\n2.返回主菜单\n请选择:'))
        if idx == 1:
            grammar_checker.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字！')
    
    elif op == 7:
        idx = eval(input('\n------------菜单七------------\n1.输入网址\n2.返回主菜单\n请选择:'))
        if idx == 1:
            pach.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字！')

    elif op == 8:
        idx = eval(input('\n------------菜单八------------\n1.输入参数\n2.返回主菜单\n请选择:'))
        if idx == 1:
            competition.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字！')
    
    
main()
