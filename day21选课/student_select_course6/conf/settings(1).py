import os

base = os.path.dirname(os.path.dirname(__file__))
db = os.path.join(base,'db')
log = os.path.join(base,'log')
student_info = os.path.join(db,'student_info')
course_info = os.path.join(db,'course_info')
userinfo = os.path.join(db,'userinfo')
log_path =  os.path.join(log,'log.log')
log_level = 'DEBUG'
