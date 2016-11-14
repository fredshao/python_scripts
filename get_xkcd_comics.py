#coding=utf-8
import urllib
import re

start = 1614
end = 1656
prevUrl = 'http://xkcd.com/'

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImgUrl(html):
	reg = r'src="(.+?\.png)" title='
   	imgre = re.compile(reg)
   	imglist = re.findall(imgre,html)
   	if(len(imglist) > 0):
   		return imglist

   	reg = r'src="(.+?\.jpg)" title='
   	imgre = re.compile(reg)
   	imglist = re.findall(imgre,html)
   	
   	return imglist    

  
def getImg(url,name):
	conn = urllib.urlopen(url)
	f = open(name,'wb')
	f.write(conn.read())
	f.close()
	


def loopPrintUrl(imglist):
	for imgurl in imglist:
		url = 'http:' + imgurl
		print (url)


def getImgFileNameFromUrl(url):
	strlist = url.split('/')
	return strlist[4]
	



def loopDownLoadXKCDImg():
	for i in range(start,end + 1):
		downloadUrl = prevUrl + str(i) + '/'
		#print(downloadUrl)
		html = getHtml(downloadUrl)
		#print(html)
		urlList = getImgUrl(html)
		for tmpurl in urlList:
			filename = str(i)+ "_" + getImgFileNameFromUrl(tmpurl)
			imgDownLoadurl = "http:" + tmpurl
			getImg(imgDownLoadurl,filename)
			print (str(i) + "    " + imgDownLoadurl + " -> down")

loopDownLoadXKCDImg()

