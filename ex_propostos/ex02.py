horas = input('Informe as horas: ')

try:
    horas = int(horas)
    if 0 <= horas <= 11:
        print('Bom dia!')

    elif 12 <= horas <= 17:
        print('Boa tarde!')

    elif 18 <= horas <= 23:
        print('Boa noite!')

    elif horas < 0 or horas > 23:
        print('Horário inválido!')

except:
    print('Valor inválido.')
