import logging
import sys
# 输出到控制台（二选一）
# logging.basicConfig(format='%(asctime)s - %(pathname)s : [line:%(lineno)d] - %(levelname)s:%(message)s',level=logging.INFO,encoding='utf8')

# logging.info('info')
# logging.debug('debug')
# logging.warning('warning')


# 输出到文件  （二选一）
logging.basicConfig(filename='log.txt',filemode='w',encoding='utf8',level=logging.DEBUG,format='%(asctime)s - %(pathname)s : [line:%(lineno)d] - %(levelname)s:%(message)s')

logging. info(  'info')
logging.debug('debug')
logging.warning('warning')
print(sys.path)