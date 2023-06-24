# sourcery skip: avoid-builtin-shadow
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh = logging.FileHandler(filename='./log1.txt',mode='w',encoding='utf8')
fh.setLevel(logging.WARNING)
format = logging.Formatter('%(asctime)s - %(pathname)s : [line:%(lineno)d] - %(levelname)s:%(message)s')
fh.setFormatter(format)
sh.setFormatter(format)
logger.addHandler(fh)
logger.addHandler(sh)

logger.debug('')
logger.info('')
logger.warning('')
logger.error('')
logger.critical('')