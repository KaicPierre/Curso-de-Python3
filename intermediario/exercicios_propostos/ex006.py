# Utilizando *args e **kwargs para repassar argumentos para outras funções

def falar(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

def function_master(func, *args, **kwargs):
    return func(*args, **kwargs)

exec = function_master(falar, 'Kaic')
exec2 = function_master(saudacao, 'Kaic', saudacao='Bom Dia')
print(exec)
print(exec2)


