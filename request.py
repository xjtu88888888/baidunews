#������һ����ȡ��������ڰٶ��ϵ����ŵ����ݵĳ���
import requests
from lxml import html
import pickle

objs = ["�η�","�Ż�","��˹��","����Ͱ�","��Ѷ","�ٶ�","����","�滢360","�Ѻ�","����","����","Я��","ͨ�õ���","AT&T","Verizon","����","�ֶ���","NTT","�ȸ�","΢��","�׹���","������","˼��","����ѷ","ƻ��","����","����","����","Ӣ�ض�","��Ϊ","ŵ����","����","����","��ͨ","��","������","IBM","5G","ͨ�Ƽ��ı�","��������","δ���Ƽ�","���ʽ","����","���","����","����","ͨ��","������","���ܼҾ�","�˹�����","VR","��������","����оƬ","�Ƽ���","�û�����","���","��ҵ","������","�Ƽ�����","�ɴ����豸","��ʾ����"];
f = open('G:/test/news201702190002.txt', 'a')   
for obj in objs:
   #ƴ�Ӳ���
   payload = {'tn': 'newstitle', 'word': obj,'rn': '50'}
   #��ȡ����ҳ��
   response = requests.get("http://news.baidu.com/ns", params=payload)
   #�޸ı����ʽ
   response.encoding = 'utf-8'
   #print response.encoding
   #��ӡ��ҳ�����ַ
   #print(response.url)
   #��ȡҳ������
   msg = response.text
   #ȥ������ɵı�ǩ
   msg =msg.replace('<em>', '')
   msg =msg.replace('</em>', '')
   msg =msg.replace('result title titlelast', 'result title')
   #print msg
   tree = html.fromstring(msg)
   
   #���ڴ��л�ȡ������
   titles = tree.xpath('//div[@class="result title"]/h3/a/text()')
   links = tree.xpath('//div[@class="result title"]/h3/a/@href')
   '''
   �����������
   print 'Titles: ', titles
   #print 'Links: ', links
   '''
      #д�ļ�

   for num in range(0,len(titles)):
      f.write(titles[num] + ';' + links[num] + '\n') 
f.close()   