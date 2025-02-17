from math import log, atan


def main(y):
    if(y < -28):
        return(pow(y, 2) - 77*pow(log(y), 4))
    elif(-28 <= y and y < 28):
        return(1-20*(pow(round(y), 7)) - 23*(pow(round(y), 6)))
    elif(28 <= y and y < 67):
        return(pow(y, 2) - 31 - 47*(pow(y, 3)))
    elif(67 <= y and y < 140):
        return(72*(pow(y, 3) - 36))
    elif(y > 140):
        return(91*(pow(81*pow(y, 2), 7)) - 7*pow(atan(73*y), 3))


'''
print(main(196))  # = 2.57e+47
print(main(144))  # = 3.43e+45
print(main(9))  # = -1.08e+08
print(main(177))  # = 6.17e+46
print(main(137))  # = 1.85e+08
'''
