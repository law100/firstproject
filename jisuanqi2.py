import random as rm
while True:
    print('1 加法')
    print('2 减法')
    print('3 乘法')
    print('4 除法')
    print('5 随机')
    choice=input('请输入你的选择')

    if choice=='5':
        choice=str(rm.randint(1,4))
        if choice=='1':
            x=float(input('请输入第一个加数'))
            y=float(input('请输入第二个加数'))
            result=x+y
        elif choice=='2':
            x=float(input('请输入被减数'))
            y=float(input('请输入减数'))
            result=x-y
        elif choice=='3':
            x=float(input('请输入第一个因数'))
            y=float(input('请输入第二个因数'))
            result=x*y
        elif choice=='4':
            x=float(input('请输入被除数'))
            y=float(input('请输入除数'))
            while y==0:
                input('除数不能为0，按回车继续')
                y=float(input('请输入除数'))
            result=x/y
    else:
        if choice=='1':
            x=float(input('请输入第一个加数'))
            y=float(input('请输入第二个加数'))
            result=x+y
        elif choice=='2':
            x=float(input('请输入被减数'))
            y=float(input('请输入减数'))
            result=x-y
        elif choice=='3':
            x=float(input('请输入第一个因数'))
            y=float(input('请输入第二个因数'))
            result=x*y
        elif choice=='4':
            x=float(input('请输入被除数'))
            y=float(input('请输入除数'))
            while y==0:
                input('除数不能为0，按回车继续')
                y=float(input('请输入除数'))
            result=x/y
        else:
            break
     

    choicee=input('是否保留小数\n1:保留\n2:不保留')
    if choicee=='1':
        r=int(input('请输入保留小数位数，输入零保留整数'))
        if r==0:
            result=round(result)
        else:
            result=round(result,r)
    else:
        if choicee=='2':
            z=result%1
            if z==0:
                result=round(result)
        else:
            print('您输入了不符合设定的东西，系统生气了，保留原状！')
        
    print('结果是',result)
    ct=input('是否继续？（y/n）')
    if ct=='n':
        break
    else:
        continue
input('程序运行完毕，按回车键退出程序...')
