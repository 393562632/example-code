fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)

# 默认升序排列
fruits = sorted(fruits)
print(fruits)

# 降序排列
fruits = sorted(fruits, reverse=True)
print(fruits)

# 按照长度由小到大排序
fruits = sorted(fruits, key=len)
print(fruits)

# 按照长度由大到小排序
fruits = sorted(fruits, key=len, reverse=True)
print(fruits)