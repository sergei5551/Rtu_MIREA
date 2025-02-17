def fast_mul(x1, x2):
    # Нахождение строк умножения
    list_str_mul = list()
    for i in range(len(str(x1))):
        sum_str_current = ""
        for j in range(len(str(x2))):
            x1_aditi = x1
            ost_x1 = x1_aditi%10
            x1_aditi //= 10

            sum_str_current += str(x2%10 * ost_x1)
        x1 //= 10
        sum_str_current += "0"*i
        list_str_mul.append(sum_str_current)

    # Сложение строк умноженных чисел
    sum = 0
    for i in range(len(list_str_mul)):
        sum += int(list_str_mul[i])

    uncorrected_mean = list(str(sum))
    # Нахождение правильного бинарного числа при умножении
    for i in range(len(uncorrected_mean)-1, 0-1, -1):
        print(uncorrected_mean, i)
        if(uncorrected_mean[i] == '0' or uncorrected_mean[i] == '1'):
            continue
        elif(int(uncorrected_mean[i]) >= 2):

            if (i == 0):
                uncorrected_mean[i] = '0'
                uncorrected_mean.insert(0, '1')
            else:
                if(int(uncorrected_mean[i]) == 3):
                 uncorrected_mean[i] = '1'
                else:
                 uncorrected_mean[i] = '0'
                uncorrected_mean[i-1] = str(int(uncorrected_mean[i-1])+1)
    print(uncorrected_mean, "итог")
    return "".join(uncorrected_mean)


print(fast_mul(101, 111)) # 5 * 7 = 35
