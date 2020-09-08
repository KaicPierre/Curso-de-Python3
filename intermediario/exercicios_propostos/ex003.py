def aumento_percentual (n1, percent):

    if float(n1) and float(percent):
        return n1 + n1 * (percent/100)
    else:
        return

var = aumento_percentual(100, 10)
print(var)
