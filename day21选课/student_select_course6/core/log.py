import logging
from conf.settings import log_path,log_level
class Log():
    logger = logging.getLogger()
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(log_path,encoding='utf-8')

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if hasattr(logging,log_level):
        print('set level')
        logger.setLevel(logging.DEBUG)
        fh.setLevel(getattr(logging,log_level))

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
    logger.addHandler(ch)