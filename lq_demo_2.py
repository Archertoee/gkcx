__author__ = 'StarDust'
import lq_data
import threading
import lq_lib
import time
import sys



#多线程
class thread_toGetMark(threading.Thread):

    yymm = "9501"
    khd = "1802101001"

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        birth_len = len(lq_data.birth_ym)
        for i in range(0,birth_len - 1):
            self.yymm = lq_data.birth_ym[i];
            stu_data = lq_lib.getIno(self.khd,self.yymm)
            checkAccess = lq_lib.isAccessibleData(stu_data)
            # 有效结果
            if checkAccess == 1:
                stu_school = lq_lib.getSchool(stu_data)
                if stu_school == "华南师范大学":
                    stu_num = lq_lib.getNum(stu_data)
                    stu_name = lq_lib.getName(stu_data)
                    student_result = stu_num + " " + stu_name + " " + self.yymm +" " + stu_school
                    print(student_result)
                break





def run_pro():
    sys.stderr = None # 不输出错误信息
    zkzh_len = len(lq_data.zkzh_nums)
    j = 0
    p = 0
    sleep_time = 0
    while j<zkzh_len - 1:

        # 每执行
        if j % 50 == 0:
            time.sleep(10)
        if j - p < 10:  # 前20个线程
            sleep_time = 0.1
        elif j - p < 20:
            sleep_time = 0.2
        elif j - p < 30:
            sleep_time = 0.5
        elif j - p < 40:
            sleep_time = 0.8
        elif j - p < 60:
            sleep_time = 1
        elif j - p < 100:
            sleep_time = 1.5
        else:
            sleep_time = 1.8

        thread1 = thread_toGetMark()
        thread1.khd = lq_data.zkzh_nums[j]
        thread1.start()

        j = j+1
        time.sleep(sleep_time)
run_pro()