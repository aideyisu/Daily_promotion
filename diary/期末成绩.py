

def getit(A):
    print(A)
    if(A == 100):
        return 5.0
    elif(A >= 95):
        return 4.5
    elif(A >= 90):
        return 4.0
    elif(A >= 85):
        return 3.5
    elif(A >= 80):
        return 3.0
    elif(A >= 75):
        return 2.5
    elif(A >= 70):
        return 2.0
    elif(A >= 65):
        return 1.5
    elif(A >= 60):
        return 1.0
    else:
        return 0


总学分 = 35.5 #1->英语 2->选修
电工 = 0
数字逻辑 = 0
数据结构 = 0
汇编 = 0
信息论 = 0
离散 = 0
大英 = 0
毛概 = 0
形势政策 = 0
体育 = 0
选修1 = 0
选修2 = 0
选修数量 = 0
英语六级 = 0
print("\n初始化结束\n")
选修数量 = int(input("选修数量"))
英语六级 = int(input("六级通过情况 通过为1，未过为0"))
电工 = int(input("电工"))
数字逻辑 = int(input("数字逻辑"))
数据结构 = int(input("数据结构"))
汇编 = int(input("汇编"))
信息论 = int(input("信息论"))
离散 = int(input("离散"))
大英 = int(input("大英"))
毛概 = int(input("毛概"))
形势政策 = int(input("形势政策"))
体育 = int(input("体育"))
print("Over！")
if(选修数量 == 2):
    总学分 = 总学分 
    选修1 = int(input("选修1"))
    选修2 = int(input("选修2"))
    选修1 = getit(选修1)
    选修2 = getit(选修2)
elif(选修数量 == 1):
    总学分 = 总学分 - 2
    选修1 = int(input("选修1"))
    选修1 = getit(选修1)
elif(选修数量 == 0):
    总学分 = 总学分 - 4
    选修1 = 0
    
#------------------------------------#
print(电工)
电工 = getit(电工)
数字逻辑 = getit(数字逻辑)
数据结构 = getit(数据结构)
汇编 = getit(汇编)
信息论 = getit(信息论)
离散 = getit(离散)
大英 = getit(大英)
if(英语六级 == 1):
    大英 = 大英 * 2
    总学分 += 2

毛概 = getit(毛概)
形势政策 = getit(形势政策)
体育 = getit(体育)
    



电工 = 4 * 电工
数字逻辑 = 3 * 数字逻辑
数据结构 = 4 * 数据结构
汇编 = 3 * 汇编
信息论 = 2.5 * 信息论
离散 = 4 * 离散
大英 = 2 * 大英
毛概 = 6 * 毛概
形势政策 = 2 * 形势政策
体育 = 1 * 体育
选修1 = 2 * 选修1
选修2 = 2 * 选修2

总绩点 = 电工 + 数字逻辑 + 数据结构 + 汇编 + 信息论 + 离散 + 大英 + 毛概 + 形势政策 + 体育 + 选修1 + 选修2


print(总绩点 / 总学分)
