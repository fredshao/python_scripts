import httplib
import urlparse

def request(url,cookie=''):
	ret = urlparse.urlparse(url)
	conn = httplib.HTTPConnection(ret.netloc)
	url = ret.path
	conn.request(method='GET',url = url,headers={'Cookie':cookie})
	return conn.getresponse()


cookie_str = 'ci=10;'
url = 'http://m.maoyan.com/cinemas.json'
html_doc = request(url,cookie_str).read()
print html_doc
