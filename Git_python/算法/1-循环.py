"""「迭代 iteration」是一种重复执行某个任务的控制结构。在迭代中，
程序会在满足一定的条件下重复执行某段代码，直到这个条件不再满足"""


def for_loop(n: int) -> int:
    """for 循环"""
    res = 0
    # 循环求和 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        res += i
    return res


# for 循环是最常见的迭代形式之一，适合预先知道迭代次数时使用。


def while_loop(n: int) -> int:
    """while 循环"""
    res = 0
    i = 1  # 初始化条件变量
    # 循环求和 1, 2, ..., n-1, n
    while i <= n:
        res += i
        i += 1  # 更新条件变量
    return res


# 在 while 循环中，由于初始化和更新条件变量的步骤是独立在循环结构之外的，因此它比 for 循环的自由度更高。
# 例如在以下代码中，条件变量
#  每轮进行了两次更新，这种情况就不太方便用 for 循环实现。

def while_loop_ii(n: int) -> int:
    """while 循环（两次更新）"""
    res = 0
    i = 1  # 初始化条件变量
    # 循环求和 1, 4, ...
    while i <= n:
        res += i
        # 更新条件变量
        i += 1
        i *= 2
    return res


# 总的来说，for 循环的代码更加紧凑，while 循环更加灵活，
# 两者都可以实现迭代结构。选择使用哪一个应该根据特定问题的需求来决定。


def nested_for_loop(n: int) -> str:
    """双层 for 循环"""
    res = ""
    # 循环 i = 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        # 循环 j = 1, 2, ..., n-1, n
        for j in range(1, n + 1):
            res += f"({i}, {j}), "
    return res

# 循环中嵌套循环，每一次嵌套都是一次“升维”，将会使时间复杂度提高至“立方关系”、“四次方关系”、以此类推。
