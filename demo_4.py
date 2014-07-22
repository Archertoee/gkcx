__author__ = 'StarDust'
import lib_fun
import threading
import data
# import xlrd

def append(origin,appending):
    str = origin + appending
    return  str


def write_to_file(data):
    fileName = "student_ino.txt"
    f_out = open(fileName,'a')
    try:
        f_out.write(data)
    except Exception as e:
        print(e)
    finally:
        f_out.close()


#多线程
class thread_toGetMark(threading.Thread):

    yymm = "9501"
    khd = "1802101"


    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
         #构造考号
        for weishu in range(1,1000):
            if weishu< 10:
                weishu = "00" + str(weishu)
            elif weishu<100:
                weishu = "0" + str(weishu)
            else:
                weishu = str(weishu)

            #构造的考号为
            mykh = self.khd + weishu
            #构造的年月为
            myny = self.yymm

            stu_ino = lib_fun.getIno(mykh,myny)
            check_ino = lib_fun.isAccessibleData(stu_ino)
            #构造正确
            if check_ino == 1:
                stu_mark = lib_fun.getMark(stu_ino)
                stu_name = lib_fun.getName(stu_ino)
                stu_zkzh = lib_fun.getNum(stu_ino)
                stu_csny = myny
                my_data = stu_name+"  "+stu_zkzh+"  "+stu_csny+" "+stu_mark + "\n"
                print(my_data)
                #构造成功，跳出此循环
                break



def test():
    for m_khd in data.zkzh_nums:
        for m_birth in data.birth_ym:
            thread1 = thread_toGetMark()
            thread1.yymm = m_birth
            thread1.khd = m_khd
            thread1.start()

test()
