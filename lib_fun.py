__author__ = 'StarDust'
import http.cookiejar
import urllib.request
import urllib.parse
import json


def getIno(zkzh,csny):
    cookie = "bdshare_firstime=1403794961919; SSCSum=3; Hm_lvt_2be31ff7176cef646e9351788dc99055=1403794882,1403794962,1403841405,1403842470; Hm_lpvt_2be31ff7176cef646e9351788dc99055=1403842473"
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
    r_data = f.read().decode('utf-8')
    return r_data
    ###############################################
    #print(r_data)
    #解析返回的json数据
    #json_data = json.loads(r_data)["student"]["name"]


#获取姓名
def getName(json_str):
    json_data = json.loads(json_str)["student"]["name"]
    return json_data

#获取准考证号
def getNum(json_str):
    json_data = json.loads(json_str)["student"]["zkzh"]
    return json_data

#获取语文分数
def getChineseMark(json_str):
    json_data = json.loads(json_str)["course"][0]["cj"]
    return json_data

#获取 文科/理科 数学分数
def getMathMark(json_str):
    json_data = json.loads(json_str)["course"][1]["cj"]
    return json_data

#获取 文科/理科 综合分数
def getUnioMark(json_str):
    json_data = json.loads(json_str)["course"][2]["cj"]
    return json_data

#获取英语分数
def getEnglishMark(json_str):
    json_data = json.loads(json_str)["course"][3]["cj"]
    return json_data

#获取 文科/理科 总分数
def getMark(json_str):
    json_data = json.loads(json_str)["course"][4]["cj"]
    return json_data

#获取 判断学生 文科/理科
def isWenOrLi(json_str):
    json_data = json.loads(json_str)["course"][1]["kmmc"]
    if(json_data=="文科数学"):
        return("文科")
    else:
        return("理科")

#判断返回的数据是否是需要的数据
def isAccessibleData(json_str):
    json_data = json.loads(json_str)["flag"]
    return json_data



###############################################################################################################
#######

# 测试的例子
# zkzh2 = '180210639'
# csny2 = '9509'
#


#
# zkzh2 = '1802201501'
# csny2 = '9411'

# stuino = getIno(zkzh2,csny2)
# if(isAccessibleData(stuino) == 1):
#     print(isWenOrLi(stuino))
# else:
#     print("数据不合理！")
#
#
# stuino2 = getIno(zkzh2,csny2)
# if(isAccessibleData(stuino) == 1):
#     print(isWenOrLi(stuino2))
# else:
#     print("数据不合理！")