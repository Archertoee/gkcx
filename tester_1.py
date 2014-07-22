__author__ = 'StarDust'
import lq_data
import threading
import lq_lib
import time
import sys

myThreadList = set() #线程集合
stu_set = set()  #学生集合

#多线程
class thread_toGetMark(threading.Thread):

    yymm = "9501"
    khd = "1802101001"

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        myThreadList.add(self.khd)  # 线程集合，启动

        birth_len = len(lq_data.birth_ym)
        for i in range(0,birth_len - 1):
            self.yymm = lq_data.birth_ym[i];
            try:
                stu_data = lq_lib.getIno(self.khd,self.yymm)
            except:
                i = i -1 # 发送失败时重发
                continue
            checkAccess = lq_lib.isAccessibleData(stu_data)
            # 有效结果
            if checkAccess == 1:
                stu_school = lq_lib.getSchool(stu_data)
                if stu_school == "华南师范大学":
                    stu_num = lq_lib.getNum(stu_data)
                    stu_name = lq_lib.getName(stu_data)
                    student_result = stu_num + " " + stu_name + " " + self.yymm +" " + stu_school
                    stu_set.add(student_result + "\n")
                    print(student_result)
                break
        myThreadList.remove(self.khd)  #线程执行完毕，清除线程





def run_pro():
    sys.stderr = None # 不输出错误信息
    zkzh_len = len(lq_data.zkzh_nums)
    j = 0
    MAX_Thread_NUM = 500
    sleep_time = 0.05
    while j<zkzh_len:
        if len(myThreadList) < MAX_Thread_NUM:
            thread1 = thread_toGetMark()
            thread1.khd = lq_data.zkzh_nums[j]
            thread1.start()
            j = j+1
        time.sleep(sleep_time)


run_pro()

#  录取结果写入文件
myfile = open("mylq_result.txt","w")
myfile.write(stu_set)
myfile.close()