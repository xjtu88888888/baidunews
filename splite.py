'''
0:����ǰ�����ڽ��б���
1:��ȡ���һ�ܵ��ļ���Ȼ�󱣴浽һ���ļ�
2:����һ��ͳһ���ļ�����ȥ��
'''
#import os
#ֱ��ɾ���Ĳ��ԣ�������յĲ��ԣ�����Ҫ��һ�㡣Ŀǰѡ����������д���
#�ֻ���ʹ��ÿ�ܵ����Ķ�ʱ��������������������������������أ�


#�����е���־�ŵ�һ���ļ���
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

#��  G:/test/lastweek.txt  �����ݽ���ȥ��

newsfilter = open('G:/test/lastweek.txt'%i)
newsfilterRead = newsfilter.read()