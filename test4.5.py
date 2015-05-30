#-*-coding:utf-8-*-
#嵌套词典
import math
numberlist={
'白雪萍':{'id':'1417140301','sex':'女','age':18,'grade':80},
'董良':{'id':'1417140302','sex':'女','age':18,'grade':86},
'范佳琪':{'id':'1417140303','sex':'女','age':18,'grade':87}
}


#---------------------------------------------------
print'欢迎使用班级管理系统'
print'  1.查询全班人数'
print'  2.查询最大年龄'
print'  3.查询最小年龄'
print'  4.查询最高成绩'
print'  5.查询最低成绩'
print'  6.查询平均成绩'
print'  7.查询平均年龄'
print'  8.增加学生'
print'  9.删除学生'


A=input('请输入你要运行的操作:')
import math
if A==1:
    names=[]
    for name in numberlist.keys():
        names.append(numberlist[name])
    print '全班人数',len(names)
if A==2:
    ages=[]
    for name  in numberlist.keys():
        ages.append(numberlist[name]['age'])
    print '最大年龄',max(ages)
if A==3:
    ages=[]
    for name  in numberlist.keys():
        ages.append(numberlist[name]['age'])
    print '最小年龄',min(ages)
if A==6:
    grades=[]
    for name  in numberlist.keys():
        grades.append(numberlist[name]['grade'])
    print '平均成绩',(1.0*sum(grades)/len(grades))
if A==4:
    grades=[]
    for name  in numberlist.keys():
        grades.append(numberlist[name]['grade'])
    print '最高成绩',max(grades)
if A==7:
    ages=[]
    for name  in numberlist.keys():
        ages.append(numberlist[name]['age'])
    print '平均年龄',(1.0*sum(ages)/len(ages)) 
if A==5:
    grades=[]
    for name  in numberlist.keys():
        grades.append(numberlist[name]['grade'])
    print '最高成绩',min(grades)
if A==8:
    def add_student(name,xuehao,age,grade)
    numberlist[name]={}
    numberlist[name]['age']=age