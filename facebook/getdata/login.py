#coding:utf-8
 
import sys
import re
import urllib2
import urllib
import cookielib
  
reload(sys)
sys.setdefaultencoding("utf8")  
#####################################################
loginurl = 'http://www.shanbay.com/accounts/login/'
logindomain = 'shanbay.com'
name = "lele94218"
pwd = "19940218a"
try:
    cj = cookielib.LWPCookieJar()            
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
    urllib2.install_opener(opener)
    loginparams = {'id_username':name, 'id_password':pwd}
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    opener.addheaders([("User-agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36"),("Accept","*/*"),('Referer','http://www.google.com')])    
    req = urllib2.Request(loginurl, urllib.urlencode(loginparams))
    print "aa"
except Exception, e:
    print "error"
    print str(e)
