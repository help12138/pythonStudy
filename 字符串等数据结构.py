# 字符串

# s1 = 'hello ' * 3
# print(s1)  # 字符串可以用乘法
#
# s2 = "world"
# s1 += s2
# print(s1)  # 字符串可以用 + 号进行拼接
#
# print('ll' in s1)  # 字符串可以用 in 判断有没有存在相应字符
#
# str2 = "asdfghjkl"
# print(str2[2])  # 取出指定位置的字符， 此处为d
#
# print(str2[2:5])  # 切片运算，从下标为2的位置到5
# print(str2[2:6:2])  # 从下标为2的位置到6以步长为2的切
#

str1 = "hello, world"
# print(len(str1))  # 字符串长度用内置len()

# print(str1.capitalize())  # 首字符大写
# print(str1.title())  # 字符串中每个单词的首字符大写
# print(str1.upper())  # 所以字符大写

# print(str1.find('or'))  # 查找对应字符串出现的第一个位置, 找不到返回 -1
# print(str1.index("or"))  # 与find功能一样，但是找不到会报异常

# print(str1.startswith('he'))  # 查看字符串是否以指定字符开头，返回布尔值
# print(str1.endswith("ld"))  # 查看字符串是否以指定字符结尾，返回布尔值

# print(str1.center(20, "*"))  # 将字符串以指定宽度居中，并在两侧填充指定字符
# print(str1.rjust(20, "*"))  # 将字符串以指定宽度靠右，并在左侧填充指定字符
# print(str1.ljust(20, '*'))  # 靠左，填充右侧

# print(str1.isdigit())  # 检查字符串是否以数字组成
# print(str1.isalpha())  # 是否以字母组成
# print(str1.isalnum())  # 数字与字母

# a, b = 5, 10
# print('{0} * {1} = {2}'.format(a, b, a*b))  # 字符串的格式化
# print(f'{a} * {b} = {a * b}')  # 3.6版本以后的写法
