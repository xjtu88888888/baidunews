'''
0:按当前的日期进行备份
1:读取最近一周的文件，然后保存到一个文件
2:对这一个统一的文件进行去重
'''
#import os
#直接删除的策略，还是清空的策略？后者要好一点。目前选择在这里进行处理。
#又或者使用每周单独的定时任务来清除，而不是在在这里进行清除呢？


#将所有的日志放到一个文件中
fallinweek=file("G:/test/lastweek.txt","a+")
for i in range(0,7):
    f1=open('G:/test/news_%s.txt'%i)
    fread=f1.read()
    fallinweek.write(fread) 
    f1.close()
    
    f2=open('G:/test/news_%s.txt'%i,"w")
    f2.write("") 
    f2.close()
#    os.remove('G:/test/news_%s.txt'%i)
    i=i+1
fallinweek.close()

#对  G:/test/lastweek.txt  的内容进行去重

newsfilter = open('G:/test/lastweek.txt'%i)
newsfilterRead = newsfilter.read()