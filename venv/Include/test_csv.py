
import csv

import pytest

result_test = csv.reader(open('../data/导入.csv','r',encoding='utf-8-sig'))
print(result_test)

for csv in result_test:
    print(csv)

#pytest.main()
