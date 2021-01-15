pal = 999*999
factor_not_found = True

while factor_not_found:
    pal_str = str(pal)
    pal_reverse = pal_str[::-1]
    if pal_str == pal_reverse:
        factors = []
        for n in range(100, 1000):
            if pal % n == 0:
                factors.append(n)
        for factor in factors:
            if pal / factor in factors:
                print("largest number is {} = {} x {}".format(pal, factor, pal/factor))
                factor_not_found = False
                break
    pal += -1

