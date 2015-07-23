#HighExaminationAdmitQuery

##简介
HighExaminationAdmitQuery是用查询高考成绩和录取结果的脚本，基于Python，简单高效。

##内置功能
- 成绩查询
- 录取结果查询

##快速体验
- 下载源码
- 打开 `Score` 文件夹里面的 `Score.py` 文件，修改`get_result()`里面参数为对应的学号和出生年月，执行` get_result()`，相应结果会写入到 `Score/score.txt` 里面。
- 打开 `Admit` 文件夹里面的 `HttpRequestTool.py`， 修改 `get_admit_result_by_number_and_birthday()`里面的相应参数，执行`get_admit_result_by_number_and_birthday()`, 相应结果会写入到 `Amint/admit.txt` 里面。