from core import auth
from conf import settings
def main():
    print('欢迎来到学生选课系统')
    # 登录
    auth.login()
    import logging
    logging.basicConfig(filename=settings.log_path,level=logging.INFO)
    logging.info('login_success')