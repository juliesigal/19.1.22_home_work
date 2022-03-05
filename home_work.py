#create a singleton class called MyTimer. this class will have all the singleton stuff.

from datetime import datetime

# Singleton
# 1. cannot create more than 1 instances
# 2. when getting the object twice (or more) --> we will get the same object every time
# 3. when getting the object from two places at once it will work (later in course)

# hack the __init__

class MyTimer(object):

    # 1
    _instance = None

    # 2
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    # 3 -- see below more about class method
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.name = 'julie' # maybe from config
        return cls._instance

    # *etgar: add the following non-static methods: start_timer which will remember the current time,
    def start_timer():
        start_time = datetime.utcnow()
        return start_time

    # get_timer which will print the diff between the current time and the start time

    def get_timer(start_time):
        current_time = datetime.utcnow()
        return current_time - start_time

a = MyTimer.start_timer()
print(a)
# b = MyTimer.get_timer(a)
# print(b)