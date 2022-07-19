import os
from utils import data_util


class Person:
    def __init__(self, name="未知", age=0, gender="Male", hobbies=None, todo=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobbies = hobbies
        self.todo = todo

    def __str__(self):
        s = f"name={self.name}, age={self.age},gender={self.gender},todo={self.todo}"
        return s

    def save_json(self):
        json_data = self.__dict__
        filepath = os.path.join("data", self.name)
        os.path.exists('data') or os.mkdir('data')
        with open(filepath, "w") as fp:
            data_util.save_json_to_file(json_data, fp)


if __name__ == '__main__':
    ff = Person(name="FF", age=24, todo=["coding", "writing"])
    print(ff)
    ff.save_json()
