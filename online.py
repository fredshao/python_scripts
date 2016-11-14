import urllib2
import urllib
import os
import time
#url = "https://wlan.ct10000.com/style/ish/index.jsp?paramStr=0UvdVfQabJ%2FgHWbQiWDkWglSOh%2BfO9zwAV%2BO%2BKVF88JfDr3yx0injGMa5jLbpXXQkvrE6dPE6GxpXqBDKIzBPJbNOzxwU0zy4Y4GhpLrKnsxfL2piZNGY6DKDuk78%2BicfiXfriqHgzD9ABwxyZSUZbrwyKg6%2F2NxZl4RlHVQPjeXVlePoby74MYM13HoHJFyzvodPxXwKX3KVNKq%2Fl4hgmEzQbF%2FMoOipZrG1uCeLn21dN1y1hWRv7spBcCymsYii9JEIMpdaNINXaO1gLTPtEeK74drm9Q7BrCLOsGGLwoSqLbWPv999oG2XWvcVofkY8DcZgq0wszjoZ5TXoT1UY34mwscTyLTiB1873dy9YhiuMgmlkHQznqSQLm%2FrcQRVp9eEQh5FxQ%3D"
#f = urllib.urlopen(url)
#s = f.read()
#print s



def online():
	posturl = "https://wlan.ct10000.com//authServlet"
	phone = "18516359414"
	password="8015"
	params_str = "QAcMcmUlGW68MioOv9jcRcp5+VMTlyjU6xeOI7pdiiuLbWrh1wYxEp5x2QXhYYeGWN66VhBcVtv1KfExfnRZdFL3VX0Gmyf4B1m0Ilg5FoJUjofnzvc8AFfjvilRfPCXw698sdIp4xjGuYy26V10JL6xOnTxOhsUNTPAofJTJnqUmu6Zdwo2eL2ZUMisy/tJcTOvk+xnGIz0/0gHAznw3YrNSLkP3jU5iQwN9YJzUBpsb0niG+eIUfzvJY3lGTQK4w9/CE2PrWf02DZhVgsq9bCvkakkzCmz5N9KbXqYVKJNN9KHCMbx81dZ6VN28v31RbtSVs9Kq4GsIs6wYYvChKottY+/332gbZda9xWh+TJ0mMUpZJ7qf2yZHiz1jtZwey4DdeMfeY="
	params_str_enc = "%2FQAcMcmUlGW68MioOv9jcRcp5%2BVMTlyjU6xeOI7pdiiuLbWrh1wYxEp5x2QXhYYeGWN66VhBcVtv1KfExfnRZdFL3VX0Gmyf4B1m0Ilg5FoJUjofnzvc8AFfjvilRfPCXw698sdIp4xjGuYy26V10JL6xOnTxOhsUNTPAofJTJnqUmu6Zdwo2eL2ZUMisy%2FtJcTOvk%2BxnGIz0%2F0gHAznw3YrNSLkP3jU5iQwN9YJzUBpsb0niG%2BeIUfzvJY3lGTQK4w9%2FCE2PrWf02DZhVgsq9bCvkakkzCmz5N9KbXqYVKJNN9KHCMbx81dZ6VN28v31RbtSVs9Kq4GsIs6wYYvChKottY%2B%2F332gbZda9xWh%2BTJ0mMUpZJ7qf2yZHiz1jtZwey4DdeMfeY%3D"
	
	params = urllib.urlencode({'paramStr':params_str,'paramStrEnc':params_str_enc,'province':'telecom.dynamic@ish','prefix':'NE','logintype':2,'UserName':phone, 'PassWord': password})
	request = urllib.urlopen(posturl,params)
	print request.read()


while(1):
	return1 = os.system('ping -c 2 www.baidu.com')
	if return1:
		online()
	else:
		print "ping ok"
	time.sleep(10)