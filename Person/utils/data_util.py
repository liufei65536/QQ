# todo
# 数据读取、存储相关

import json
from models.person import Person

# 保存json数据 到文件
def save_json_to_file(json_data, fp):
    json.dump(json_data, fp, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    ff = Person(name="FF", age=24, todo=["coding", "writing"])
    with open("today","w") as fp:
        save_json_to_file(ff.get_json(), fp)
