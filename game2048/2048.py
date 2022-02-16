"""
2048 游戏核心算法
"""

list_merge = [2, 0, 2, 0]
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2],
]

def zero_to_end():
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

def merge():
    """
    合并
    先将零移至末尾
    然后合并相邻相同数字
    :return:
    """
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)

def move_left():
    """
    全局变量只能用不能在函数里面改，如果要在函数里面改需要先用global改为全局
    :return:
    """
    for line in map:
        global list_merge
        list_merge = line
        merge()

def move_right():
    for line in map:
        global list_merge
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge

def square_matrix_transpose(sqr_matrix):
    """
    方阵转置
    :param sqr_matrix:
    :return:
    """
    for c in range(1, len(sqr_matrix)):
        for r in range(c, len(sqr_matrix)):
            sqr_matrix[r][c-1], sqr_matrix[c-1][r] = sqr_matrix[c-1][r], sqr_matrix[r][c-1]

def move_up():
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)

def move_down():
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)

move_down()
def result_2048():
    for i in range(len(map)):
        print(map[i])
result_2048()
