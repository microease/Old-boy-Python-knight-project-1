import pickle
from core.student import Student
from core.base import Person
from core.course import Course
from conf.settings import *
from core.log import Log
class Manager(Person):
    operate_lst = [('创建课程','create_course'),
                   ('创建学生','create_student'),
                   ('查看所有课程','show_courses'),
                   ('查看所有学生','show_students'),
                   ('查看所有学生的选课情况','show_student_course'),
                   ('退出','exit')]
    def __init__(self,name):
        self.name = name

    def create_course(self):
        name = input('course name : ')
        price = input('course price : ')
        period = input('course period : ')
        teacher = input('course teacher : ')
        course_obj = Course(name,price,period,teacher)
        self.dump_obj(course_info, course_obj)
        print('%s课程创建成功'%course_obj.name)

    def create_student(self):
        # 用户名和密码记录到userinfo文件，将学生对象存储在student_info文件
        stu_name =input('student name : ')
        stu_pwd =input('student password : ')
        stu_auth = '%s|%s|Student\n'%(stu_name,stu_pwd)
        stu_obj = Student(stu_name)
        with open(userinfo,'a',encoding='utf-8') as f:
            f.write(stu_auth)
        self.dump_obj(student_info, stu_obj)
        print('%s学生创建成功'%stu_obj.name)
        Log.logger.info('创建了一个学生%s'%stu_obj.name)

    def show_students(self):
        for count,stu in enumerate(self.get_from_pickle(student_info),1):
            print(count,stu)

    def show_student_course(self):
        for stu in self.get_from_pickle(student_info):
            print(repr(stu))

    def exit(self):
        exit()

    @classmethod
    def init(cls,name):
        return cls(name)   # 管理员的对象
