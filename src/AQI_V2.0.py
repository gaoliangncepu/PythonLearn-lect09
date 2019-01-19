# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name: AQI_V2.0
   Description: 
   Author: Administrator
   date: 2019/1/19
-------------------------------------------------
   Change Activity:
         2019/1/19:
-------------------------------------------------
"""
import json


def process_json_file(file_path):
    global city_list
    all_file_path = "../resource/" + file_path

    with open(all_file_path, 'r', encoding='utf-8') as src_file:
        city_list = json.load(src_file)  # load 对象为打开的文件，返回 list

        json_str = city_list[0]
        print(str(json_str).replace("\'", "\""))
        city_list2 = json.loads(str(json_str).replace("\'", "\""))  # 必须是双引号
        print(type(city_list2))  # dictionary 字典类型
        print(city_list2)
    return city_list


def main():
    """
        主函数
    """
    file_path = input("请输入json文件名称（包含后缀）：")
    city_list = process_json_file(file_path)
    city_list.sort(key = lambda city : city['aqi'])  # 排序，默认升序
    top5_list = city_list[:5]

    with open('../resource/top5_list.json', 'w', encoding='utf-8') as dest_file:  # encoding 指定写出文件编码方式
        json.dump(top5_list, dest_file, ensure_ascii=False)  #ensure_ascii为False，原样输出。
        top1_str = json.dumps(top5_list)
        print(type(top1_str))  # str 类型
        print(top1_str)


if __name__ == "__main__":
    main()
