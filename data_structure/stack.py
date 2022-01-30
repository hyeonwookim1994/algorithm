stack_list = []


def push(data):
    stack_list.append(data)


def get():
    if len(stack_list) == 0:
        return 'Null'
    return stack_list[-1]


def pop():
    if len(stack_list) == 0:
        return 'Null'
    fix = stack_list[-1]
    stack_list.remove(fix)
    return fix

push(1)
push(2)
push(3)
print(get())
print(pop())
print(pop())
print(pop())
print(get())
push(4)
print(pop())
print(pop())

# 3
# 3
# 2
# 1
# Null
# 4
# Null
