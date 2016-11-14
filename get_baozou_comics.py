import urllib
import re
import os

start = 1
end = 100

prevUrl = "http://baozoumanhua.com/all/hot/page/"
gstr = '" src='

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html


def getAllComicFromPage(html):
	reg = r'http://wanzao2.b0.upaiyun.com/system/pictures/\d{8}/original/.*"\ssrc='
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	return imglist


def getCorrectUrl(originUrl):
	return originUrl.replace(gstr,"")


def getImg(url,name):
	conn = urllib.urlopen(url)
	f = open(name,'wb')
	f.write(conn.read())
	f.close()


def test():
	downloadUrl = prevUrl + str(1)
	html = getHtml(downloadUrl)
	urlList = getAllComicFromPage(html)
	for tmpurl in urlList:
		finalUrl = getCorrectUrl(tmpurl)
		print finalUrl


def getFileName(imgUrl):
	index = imgUrl.rfind('/')
	name = imgUrl[index + 1:]
	return name


def loopDownLoadBaoZouComics():
	for i in range(start,end + 1):
		downloadUrl = prevUrl + str(i)
		html = getHtml(downloadUrl)
		urlList = getAllComicFromPage(html)
		for tmpurl in urlList:
			finalUrl = getCorrectUrl(tmpurl)
			name = getFileName(finalUrl)
			if (False == os.path.exists(name)):
				print finalUrl + "  ->  Download"
				getImg(finalUrl,name)
			else:
				print finalUrl + "  ->  Exist"

				
			
			

#test()

loopDownLoadBaoZouComics()
#getFileName("http://wanzao2.b0.upaiyun.com/system/pictures/35493796/original/1462174900_460x1685.jpg")