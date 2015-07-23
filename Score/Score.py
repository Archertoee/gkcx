import urllib.request
import urllib.parse
import json


def get_result(number, birthday):
    cookie = "Hm_lvt_2be31ff7176cef646e9351788dc99055=1437448597; Hm_lpvt_2be31ff7176cef646e9351788dc99055=1437450310; PHPSESSID=fblmt7m54ehe2m0q65otdfbbg5"
    url = "http://www.5184.com/gk/common/get_mem.php"
    post_data = urllib.parse.urlencode({'csny': birthday, 'zkzh': number, 'yzm': ''})
    post_data = post_data.encode('utf-8')
    request = urllib.request.Request(url)

    # make the request header.
    request.add_header("Host", "www.5184.com")
    request.add_header("Connection", "keep-alive")
    request.add_header("Content-Length", "31")
    request.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
    request.add_header("Origin", "http://www.5184.com")
    request.add_header("X-Requested-With", "XMLHttpRequest")
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36")
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    request.add_header("Referer", "http://www.5184.com/gk/index.html")
    request.add_header("Accept-Encoding", "gzip,deflate,sdch")
    request.add_header("Accept-Language", "zh-CN,zh;q=0.8")
    request.add_header("Cookie", cookie)

    f = urllib.request.urlopen(request, post_data)
    r_data = f.read().decode('utf-8')

    score_json = json.loads(r_data)
    if 'student' in score_json.keys():
        student = score_json['student']
        score = score_json['course']
        file = open('score.txt', 'a')
        file.write(student['zkzh'] + ' ' + student['name'] + '>>>')
        for i in score:
            file.write(i['kmmc'] + ' ' + i['cj'] + ' ')
        file.write('\n')
        file.close()

get_result('1802101576' ,'9802')