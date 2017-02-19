#下面是一个获取多个内容在百度上的新闻的内容的程序
import requests
from lxml import html
import pickle
import datetime

#调查对象
#objs = ["奈飞","雅虎","特斯拉","阿里巴巴","腾讯","百度","京东","奇虎360","搜狐","网易","新浪","携程","通用电器","AT&T","Verizon","惠普","沃尔玛","NTT","谷歌","微软","甲骨文","爱立信","思科","亚马逊","苹果","三星","软银","索尼","英特尔","华为","诺基亚","推特","脸书","高通","大疆","西门子","IBM","5G","通科技改变","便利生活","未来科技","生活方式","革新","变革","网络","中兴","通信","机器人","智能家居","人工智能","VR","海底网络","量子芯片","云计算","用户体验","硅谷","创业","大数据","科技创新","可穿戴设备","显示技术"];
objs = ["奈飞"]
#时间戳，写入文件名

nowtime =  datetime.datetime.now()
weekdate = nowtime.weekday()
nowdate = nowtime.strftime("%Y%m%d_%H%M_%S")

f = open('G:/test/news_%s.txt'%nowdate, 'a')   
flog = open('G:/test/news_%s.txt'%weekdate, 'a')  #注意在这个重写之前要进行去重

for obj in objs:
   #拼接参数
   payload = {'tn': 'newstitle', 'word': obj,'rn': '50'}
   #获取到该页面
   response = requests.get("http://news.baidu.com/ns", params=payload)
   #修改编码格式
   response.encoding = 'utf-8'
   #print response.encoding
   #打印该页面的网址
   #print(response.url)
   #获取页面内容
   msg = response.text
   #去除不相干的标签
   msg =msg.replace('<em>', '')
   msg =msg.replace('</em>', '')
   msg =msg.replace('result title titlelast', 'result title')
   #print msg
   tree = html.fromstring(msg)
   
   #在内存中获取到数据
   titles = tree.xpath('//div[@class="result title"]/h3/a/text()')
   links = tree.xpath('//div[@class="result title"]/h3/a/@href')
   '''
   检查数据内容
   print 'Titles: ', titles
   #print 'Links: ', links
   '''
      #写文件
   for num in range(0,len(titles)):
      f.write(titles[num] + ';' + links[num] + '\n') 
      flog.write(titles[num] + ';' + links[num] + '\n') 
f.close()   
flog.close()