__author__ = 'StarDust'
import lq_data
import threading
import lq_lib
import time
import xlrd

#多线程
class thread_toGetMark(threading.Thread):

    yymm = "9501"
    khd = "1802101001"
    finished = "yes"

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        stu_data = lq_lib.getIno(self.khd,self.yymm)
        checkAccess = lq_lib.isAccessibleData(stu_data)
        # 有效结果
        if checkAccess == 1:
            stu_school = lq_lib.getSchool(stu_data)
            if stu_school == "华南师范大学":
                stu_num = lq_lib.getNum(stu_data)
                stu_name = lq_lib.getName(stu_data)
                student_result = stu_num + " " + stu_name + " " + stu_school
                print(student_result)


def run_pro():
    zkzh_len = len(lq_data.zkzh_nums)
    birth_len = len(lq_data.birth_ym)



run_pro()

# def test():
#     for m_khd in lq_data.zkzh_nums:
#         # 设置时间间隔，防止被服务器识别
#         time.sleep(6)
#         print(m_khd)
#         for m_birth in lq_data.birth_ym:
#             thread1 = thread_toGetMark()
#             thread1.yymm = m_birth
#             thread1.khd = m_khd
#             time.sleep(0.1)
#             thread1.start()
#
#
# test()

# # 读取数据
# data = xlrd.open_workbook('gk.xls')
# #通过索引顺序获取
# table = data.sheets()[0]
# nrows = table.nrows
# for i in range(1,nrows-1):
#     kh = table.cell(i,0).value
#     kh = int(kh)
#     print(str(kh) + ",")
