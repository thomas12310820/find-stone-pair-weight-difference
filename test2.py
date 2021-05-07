# -*- coding: utf-8 -*-
"""
Created on Tue May 2 20:16:00 2021

@author: TG
"""
from random import randint


def start():
    print("解题思路：\n"
          "1. 自定义N块石头，每块石头的重量随机定义。\n"
          "2. 对石头按照重量进行排序，从小到大。\n"
          "3. 输入需要的重量差。\n"
          "4. 排序好的石头列表按照从小到大的顺序遍历元素。\n"
          "5. 每次遍历都判断当前元素加上之前定义的重量差值，结果寻找后面列表内容是否有相匹配的。\n"
          "6. 找到匹配项后保存双方的石头编号。\n")
    print("_______________________________________________________________________________________________\n")
    print("_______________________________________________________________________________________________\n\n")
    para_input()


def para_input():
    stone_list = []
    stone_count = int(input("请输入石头的数量：\n"))
    for i in range(stone_count):
        stone_list.append([i+1,randint(1,50)])
    print("_______________________________________________________________________________________________\n")
    print("_______________________________________________________________________________________________\n\n")
    print("生成的石头的编号/重量如下：")
    for item in stone_list:
        print(item)

    print('\n')
    print("对上述按照重量由低到高排序结果如下：")
    stone_list.sort(key=lambda item: item[1])
    for item in stone_list:
        print(item)
    print("_______________________________________________________________________________________________\n")
    print("_______________________________________________________________________________________________\n\n")
    loop_start(stone_list)


def loop_start(stone_list):
    loop = True
    while loop:
        delta_weight = input("请输入想要查询的重量差，取消退出输入q：\n")
        if delta_weight == 'q':
            loop = False
        elif delta_weight.isdigit():
            get_result(int(delta_weight),stone_list)
            print("_______________________________________________________________________________________________\n")
            print("_______________________________________________________________________________________________\n")
        else:
            pass


def get_result(delta_weight,stone_list):
    result_list = []
    for index in range(len(stone_list)):
        up_weight = stone_list[index][1] + delta_weight
        for index_after in range(index,len(stone_list),1):
            if stone_list[index_after][1] == up_weight:
                result_list.append([stone_list[index][0],stone_list[index_after][0]])
            else:
                pass
    print("{}的重量差的石头对分析结果如下：".format(delta_weight))
    print(result_list)






if __name__ == '__main__':
    start()