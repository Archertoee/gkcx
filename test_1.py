__author__ = 'StarDust'
import urllib.request
import urllib.parse


cookie = "bdshare_firstime=1403794961919; SSCSum=3; Hm_lvt_2be31ff7176cef646e9351788dc99055=1403794882,1403794962,1403841405,1403842470; Hm_lpvt_2be31ff7176cef646e9351788dc99055=1403842473"
zkzh = '1802201501'
csny = '9411'
url = "http://www.5184.com/gk/common/get_mem_1.php"
postdata = urllib.parse.urlencode({'csny':csny,'zkzh': zkzh,'yzm': '12'})
postdata = postdata.encode('utf-8')
request = urllib.request.Request(url)
#构造http头部
request.add_header("Host","www.5184.com")
request.add_header("Connection","keep-alive")
request.add_header("Content-Length","31")
request.add_header("Accept","application/json, text/javascript, */*; q=0.01")
request.add_header("Origin","http://www.5184.com")
request.add_header("X-Requested-With","XMLHttpRequest")
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36")
request.add_header("Content-Type","application/x-www-form-urlencoded")
request.add_header("Referer","http://www.5184.com/gk/check_index.html")
request.add_header("Accept-Encoding","gzip,deflate,sdch")
request.add_header("Accept-Language","zh-CN,zh;q=0.8")
request.add_header("Cookie",cookie)

f = urllib.request.urlopen(request,postdata)
print(f.read().decode('utf-8'))

