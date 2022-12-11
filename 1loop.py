import random
word=["随机数小游戏","系统会自动选择1到100的整数","系统会根据你的猜测情况自动打分"]
for i in word:
    print(i)
while True:
    min1=0
    max1=100
    count=0
    a=0
    num=random.randint(1,100)
    while a!=num:
        a=int(input("请猜测一个数字："))
        if a==num:
            print("恭喜你回答正确")
        elif a>num:
            max1=a
            print(min1,"~",max1)
        else:
            min1=a
            print(min1,"~",max1)
        count+=1
    if count==1:
        score="天才！！！"
    elif 1<count<8:
        score="正常水平"
    else:
        score="你没用二分法"
    print("您输入了",count,"次,",score)
    ct=input('是否继续？（y/n）')
    if ct=='n':
        break
    elif ct=='y':
        continue
    else:
        break
input("程序运行完毕，按回车键结束运行")