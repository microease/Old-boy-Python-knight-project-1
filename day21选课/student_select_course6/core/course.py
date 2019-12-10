import pickle
from core.base import Base
from conf.settings import course_info

class Course(Base):
    def __init__(self, name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

    def __repr__(self):
        return ' '.join([self.name, self.price, self.period, self.teacher])

    def show_courses(self):
        for count,course in enumerate(self.get_from_pickle(course_info),1):
            print(count,repr(course))

    def dump_obj(self,path,obj):
        with open(path,'ab') as f:
            pickle.dump(obj,f)