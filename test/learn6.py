list = [1, 2, 3]

# 获取列表长度
print(len(list))

# 列表后面添加元素
list.append(4)  # [1,2,3,4]

# 在指定位置插入元素
list.insert(1, 30)  # [1,30,2,3,4]

# 合并列表
list.extend([20])  # [1,2,3,20]
list += [200]  # [1,2,3,20,200]

# 移除指定元素
list.remove(3)  # [1, 30, 2, 4, 20, 200]

# 移除指定位置的元素
list.pop(2)  # [1, 30, 4, 20, 200]

# 清空列表
list.clear()  # []

print(list)

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1) # 正序 ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True) # 倒序 ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

print(list2)
print(list3)
print(list4)
