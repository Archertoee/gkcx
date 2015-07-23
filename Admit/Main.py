import time
import sys

from Admit import Data, ThreadPoolTool


def main():
    sys.stderr = None
    j = 0
    for number_prefix in Data.NUMBER_PREFIX:
        for number_suffix in range(0, Data.NUMBER_RANGE):
            if number_suffix < 10:
                number_suffix = '000' + str(number_suffix)
            elif number_suffix < 100:
                number_suffix = '00' + str(number_suffix)
            elif number_suffix < 1000:
                number_suffix = '0' + str(number_suffix)
            else:
                number_suffix = str(number_suffix)

            thread = ThreadPoolTool.ThreadTask()
            thread.number = str(number_prefix + number_suffix)
            thread.start()

            j += 1
            if j % 50 == 0:
                time.sleep(10)
                j = 0

# the entrance
main()
