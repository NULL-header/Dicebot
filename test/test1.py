# coding:utf-8


def adder(item, lists):
    total = int(item[2])
    for i in lists:
        if item[0] == i[1]:
            total += int(i[2])
    return total


input_number = int(input())
lists = []
for i in range(input_number):
    lists.append(input().rstrip().split(" "))

list_like = []
for i in lists:
    list_like.append(adder(i, lists))

max = 0
maxindex = 0
for i in list_like:
    if i > max:
        max = i
for i in list_like:
    if i == max:
        break
    maxindex += 1

print(lists[maxindex][0])
