def for_loop_recur(n):
    """使用迭代模拟递归"""
    # 使用一个显示的栈来模拟递归系统调用栈
    stack=[]
    res=0
    # 递：递归调用
    for i in range(n,0,-1):
        # 通过“入栈操作”模拟“递”
        stack.append(i)
    # 归：返回结果
    while stack:
        # 通过“出栈操作”模拟“归”
        res+=stack.pop()
    # res = 1+2+3+...+n
    return res


print(for_loop_recur(4))