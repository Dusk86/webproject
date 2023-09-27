import os

import pytest

if __name__ == '__main__':
    pytest.main()
    # allure generate 测试结果数据所在目录 -o 测试报告保存的目录   --clean
    # --clean 目的是先清空测试报告目录，再生成新的测试报告
    os.system("allure generate reports/tmp -o reports/report --clean")