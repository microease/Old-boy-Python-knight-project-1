import pickle
from conf.settings import course_info
class Base:
    def __str__(self):
        return self.name


class Person:
    @staticmethod
    def get_from_pickle(path):
        with open(path, 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    yield stu_obj
                except EOFError:
                    break

    def show_courses(self):
        for count, course in enumerate(self.get_from_pickle(course_info), 1):
            print(count, repr(course))

    def dump_obj(self, path, obj):
        with open(path, 'ab') as f:
            pickle.dump(obj, f)