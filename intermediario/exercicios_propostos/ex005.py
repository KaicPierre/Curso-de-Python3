def function1():
    return 'Olá, Mundo'

def function_master(func):
    return func()

exec = function_master(function1)
print(exec)




