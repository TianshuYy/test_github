"""本质上看，递归体现“将问题分解为更小子问题”的思维范式，这种分治策略是至关重要的。
从算法角度看，搜索、排序、回溯、分治、动态规划等许多重要算法策略都直接或间接地应用这种思维方式。
从数据结构角度看，递归天然适合处理链表、树和图的相关问题，因为它们非常适合用分治思想进行分析。"""


def recur(n):
    """普通递归"""
    if n == 1:
        return 1
    res = recur(n - 1)
    return n + res


def tail_recur(n, res):
    """尾递归"""
    # 终止条件
    if n == 0:
        return res
    # 尾递归调用
    return tail_recur(n - 1, res + n)


def fib(n):
    """斐波那契数列：递归"""
    # 终止条件f(1)=0,f(2)=1
    if n == 1 or n == 2:
        return n - 1
    else:
        # 递归调用 f(n)=f(n-1)+f(n-2)
        res = fib(n - 1) + fib(n - 2)
        # 返回结果 f(n)
        return res


print(recur(300))
print(tail_recur(300, 0))
print(fib(5))
