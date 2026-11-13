from abc import ABC, abstractmethod


class absclass (ABC):
    def print(self,x):
        print("Passed value:",x)
    def task(self):
        print("we are inside abc task")

class test_class(absclass):
    def task(self):
        print("we are in test_class task")

test_obj=test_class()
test_obj.task()
test_obj.print(100)


