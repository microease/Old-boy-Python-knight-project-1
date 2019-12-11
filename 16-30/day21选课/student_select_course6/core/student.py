import pickle
from core.base import Base,Person
from conf.settings import *

class Student(Person,Base):
    operate_lst = [
                   ('查看所有课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def __repr__(self):
        # course_name = [course.name for course in self.courses]
        course_name = [str(course) for course in self.courses]
        return '%s %s'%(self.name,'所选课程%s' % '|'.join(course_name))

    def select_course(self):
        self.show_courses()
        num = int(input('num >>>'))
        for count,course in enumerate(self.get_from_pickle(course_info),1):
            if count == num:
                self.courses.append(course)
                print('您选择了%s课程' % (course))
                break
        else:print('没有您要找的课程')

    def check_selected_course(self):
        for course in self.courses:
            print(course.name,course.teacher)

    def exit(self):
        with open(student_info+'_bak', 'wb') as f2:
            for stu in self.get_from_pickle(student_info):
                if stu.name == self.name:  # 如果从原文件找到了学生对象和我当前的对象是一个名字，就认为是一个人
                    pickle.dump(self, f2)  # 应该把现在新的学生对象写到文件中
                else:
                    pickle.dump(stu, f2)  # 反之，应该原封不动的把学生对象写回f2
        os.remove(student_info)
        os.rename(student_info+'_bak',student_info)
        exit()

    @classmethod
    def init(cls,name):
        for stu in cls.get_from_pickle(student_info):
            if stu.name == name:
                return stu
        else:print('没有这个学生')