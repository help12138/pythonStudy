# # 由一系列变量组成的可变序列容器
#
# list01 = ["demo1", 100, True]
# str01 = "一个新列表"
# list02 = list(str01)  # 会循环字符串里面的字符
#
# list01.append(str01)  # 添加在末尾
#
# print(list01[1:3])  # 切片
#
# list02[1:3] = ["a", "b"]  # 修改
# # 通过切片拿元素会生成新列表，修改则会在原列表上面修改
#
# print(list02, list01)
#
# # 遍历
# for i in list02:
#     print(i + "嘿嘿")

# 逐行输入你喜欢的人物
list_input = []

while True:
    str_input = input("输入你喜欢的人：")
    if str_input == "":
        break
    list_input.append(str_input)

for i in list_input:
    print(i)