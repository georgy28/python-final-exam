def pipeline(*funcs):
    def helper(arg):
        result = arg
        for func in funcs:
            result = func(result)
        return result
    return helper

################## CODE ENDS HERE ###########################

########### EXAMPLES ##############

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))
#should print 5.0

def f1(num):
    return 2*num

def f2(num):
    return num - 5

def f3(num):
    return num * num

fun2 = pipeline(f1, f2, f3)
print(fun2(4))
#should print 9

fun3 = pipeline(f3, lambda x: x * 4, f3)
print(fun3(-1))
#should print 16
print(fun3(2))
#should print 256
