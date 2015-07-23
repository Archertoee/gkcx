import urllib.request
import urllib.parse
import json

from Admit import Data


# number:the number of a student
# birthday: the student's birthday, like 9301
# try_time: the request reconnect times when it broken.
def get_admit_result_by_number_and_birthday(number, birthday, try_times=3):
    if try_times == 0:
        file = open('error.txt', 'a')
        file.write(str(number + "-" + birthday))
        return

    # make the request header.
    # all the header are copied from a normal HTTP request.
    # maybe some header is not necessary.
    cookie = "Hm_lvt_2be31ff7176cef646e9351788dc99055=1437448597;Hm_lpvt_2be31ff7176cef646e9351788dc99055=1437450310;PHPSESSID=fblmt7m54ehe2m0q65otdfbbg5"
    url = "http://www.5184.com/gk/common/get_lq_edg.php"
    post_data = urllib.parse.urlencode({'csny': birthday, 'zkzh': number, 'yzm': ''})
    post_data = post_data.encode('utf-8')
    request = urllib.request.Request(url)
    request.add_header("Host", "www.5184.com")
    request.add_header("Connection", "keep-alive")
    request.add_header("Content-Length", "31")
    request.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
    request.add_header("Origin", "http://www.5184.com")
    request.add_header("X-Requested-With", "XMLHttpRequest")
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36")
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    request.add_header("Referer", "http://www.5184.com/gk/check_lq.html")  # important. without referer, the request will return error.
    request.add_header("Accept-Encoding", "gzip,deflate,sdch")
    request.add_header("Accept-Language", "zh-CN,zh;q=0.8")
    request.add_header("Cookie", cookie)

    try:
        f = urllib.request.urlopen(request, post_data)
        r_data = f.read().decode('utf-8')
    except:
        get_admit_result_by_number_and_birthday(number, birthday, try_times - 1)

    result_json = json.loads(r_data)
    if result_json['flag'] == 1:
        result = result_json['result']
        if result['zymc'] == Data.SCHOOL:
            file = open('admit.txt', 'a')
            file.write(str(result['zkzh'] + ' ' + birthday + ' ' + result['zymc'] + ' ' + result['xm'] + '\n'))

# test
get_admit_result_by_number_and_birthday("1802301001", "9608", 1)