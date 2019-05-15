#encode utf-8
import os,sys,urllib2,re,csv,time


curPath = os.getcwd()+os.path.sep

'''
函数:获取图书信息
'''

def getBookInfo(bookname,booklink):
	html = ''
	book = []
	rISBN = re.compile(r'info_right">(\d+)</div>',re.DOTALL)
	rAuthor = re.compile('作&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;者</div>.+?info_right">(.+?)</div>'.decode('utf-8'),re.DOTALL)
	rPress = re.compile('出&nbsp;版&nbsp;社</div>.+?info_right">(.+?)</div>'.decode('utf-8'),re.DOTALL)
	rPressDate = re.compile('出版时间</div>.+?info_right">(.+?)</div>'.decode('utf-8'),re.DOTALL)
	print 'get '+bookname+'info'+'\n'
	print booklink
	os.system("pause")
	html = urllib2.urlopen(booklink).read()
	html = unicode(html,'gbk','ignore')
	if len(html) == 0:
		print 'open '+booklink+' fail'
		return 
	else:
		if len(rISBN.findall(html)) == 0 or len(rAuthor.findall(html)) == 0 or len(rPress.findall(html)) == 0 or len(rPressDate.findall(html)) == 0 :
			print 'get '+bookname+'info fail'
			return -1
			os.system('pause')
		else:
			book.append( rISBN.findall(html)[0])
			book.append( re.sub('<[^>]+>','',rAuthor.findall(html)[0].encode('gbk')) )     
			book.append( re.sub('<[^>]+>','',rPress.findall(html)[0].encode('gbk')) )
			book.append( rPressDate.findall(html)[0] )
			
			return book
				 

'''
函数:获取书目并输出至以类别和时间戳命名的csv文件中
参数:tag类别，url页码数字组成url
'''
def getBooks(tagC,urlC,pageFromC,pageToC):

	tag = tagC
	r = re.compile(r'<div class="name"><a href="(.+?)".+?title="(.+?)".+?star.+?_blank">(.+?)<.+?price_n">&yen;(.+?)<.+?price_r">&yen;(.+?)<',re.DOTALL)
	'''
	分组  0:链接,1:书名,2:评论数,3:折扣价,4:定价
	'''

	pageFrom = int(pageFromC)
	pageTo = int(pageToC)
	html = ''
	data = []
	timestamp = str(time.time())
	isbn = ''

	csvFileName = curPath + tag + timestamp+'.csv'
	csvfile = file(csvFileName,'wb')
	writer = csv.writer(csvfile)
	writer.writerow(['IDBYSALE','NAME','AUTHOR','PUB','PUBDATE','PRICE','ISBN','COMMENTS','DISCOUNT'])
	ID = 0
	for i in range(pageFrom,pageTo+1):
                url = urlC
		url = url + str(i)
		print url
		html = urllib2.urlopen(url).read()
		if len(html) == 0:
			print 'failer!fetch'+url+'fail'
			continue
		else:
			print 'yes! '+url+'\n'
			print 'begine parse data'+'\n'
			print len(r.findall(html))
			
			if len(r.findall(html)) == 0:
				print 'failer!parse fail'
			else:
				for x in r.findall(html):
					book = getBookInfo(x[1],x[0])
					if book  == -1:continue
					else:
						ID+=1
						writer.writerow([ID,x[1],book[1],book[2],book[3],x[4],book[0],x[2],x[3]])

	print 'writing csv over'		
	csvfile.close()



'''
读取要采集页面,并调用getBooks采集
'''	
webPageCsv = file(curPath+'dangdang_BS.csv','rb')
webPageCsv.readline()
reader = csv.reader(webPageCsv)
for tag,url,pageFrom,pageTo in reader:
	print 'begin fetch'+tag+pageFrom+'to'+pageTo
	getBooks(tag,url,pageFrom,pageTo)
	print tag+'done fetch'

os.system('pause')
			



			
	
