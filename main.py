import main
from Comm.Log import log_init
import logging
from Comm.data import read_excel

log_init()
logging.getLogger('main')
test = read_excel('/venv/data/导入.csv')
print(test)