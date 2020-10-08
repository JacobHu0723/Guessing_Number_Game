import random
import time
t=0
a=0
q=0
i=-1
n=-1
print("欢迎使用《请猜一个数》！\n开发者：Jacob_Hu\n本程序Github库地址:https://github.com/JacobHu0723/Guessing_Number_Game\n如有Bug请在Github下Issues进行反馈！")
print("\n")
time.sleep(1)
print("说明：\n用计算机将随机生成一个100以内的正整数，你将会有7次猜数机会。\n如果猜中了将提示“猜中了”；否则，提示数偏大或数偏小，然后继续猜数。如果7次均未猜中，将会告诉你答案，结束本次游戏。\n")
print("\n")
time.sleep(1)
while a==0:
    n=random.randint(1,100)
    print("")
    print("开始游戏！")
    print("")
    while i!=n and t!=7:
        i=int(input("请猜一个数："))
        if i==n:
            print("\033[0;32m恭喜你！猜中了！\033[0m")
            break
        if i<n and n-i>10:
            print("\033[0;31m太太太小了！\033[0m")
            t=t+1
        if i<n and n-i<=10:
            print("\033[0;31m有点小了！\033[0m")
            t=t+1
        if i>n and i-n>10:
            print("\033[0;31m太太太大了！\033[0m")
            t=t+1
        if i>n and i-n<=10:
            print("\033[0;31m有点大了！\033[0m")
            t=t+1
    if t==7:
        print("正确答案为：",n)
        print("7次没有猜中，很遗憾，游戏结束")
    print("")
    q=int(input("再玩一次？（输入1再玩一次，输入2结束游戏）"))
    if q==1:
        t=0
    else:
        a=a+1
print("")
print("感谢你的游玩！")
