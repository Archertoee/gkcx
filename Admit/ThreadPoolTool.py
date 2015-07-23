import threading

from Admit import Data, HttpRequestTool


# make one thread class to one task which get one student's result.
class ThreadTask(threading.Thread):
    number = "0"

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        birthday_length = len(Data.BIRTHDAY_PREFIX)
        for i in range(0, birthday_length - 1):
            HttpRequestTool.get_admit_result_by_number_and_birthday(self.number, Data.BIRTHDAY_PREFIX[i])

