def calculate_parameter(data):
    # i用来控制列元素，line是一行元素,j用来控制循环次数,datas用来存储局部变量。保存修改后的值
    i = 0
    j = 0
    line_size = len(data)

    # 将行列式变换为上三角行列式
    while j < line_size - 1:
        line = data[j]
        temp = line[j]
        templete = []
        for x in line:
            x = x / temp
            templete.append(x)
        data[j] = templete
        # flag标志应该进行消元的行数
        flag = j + 1
        while flag < line_size:
            templete1 = []
            temp1 = data[flag][j]
            i = 0
            for x1 in data[flag]:
                if x1 != 0:
                    x1 = x1 - (temp1 * templete[i])
                    templete1.append(x1)
                else:
                    templete1.append(0)
                i += 1
            data[flag] = templete1
            flag += 1
        j += 1

    # 求相应的参数值

    parameters = []
    i = line_size - 1
    # j标识减去元素个数
    # flag_rol标识除那一列
    rol_size = len(data[0])
    flag_rol = rol_size - 2
    # 获得解的个数
    while i >= 0:
        operate_line = data[i]
        if i == line_size - 1:
            parameter = operate_line[rol_size - 1] / operate_line[flag_rol]
            parameters.append(parameter)
        else:
            flag_j = (rol_size - flag_rol - 2)
            temp2 = operate_line[rol_size - 1]
            # result_flag为访问已求出解的标志
            result_flag = 0
            while flag_j > 0:
                temp2 -= operate_line[flag_rol + flag_j] * parameters[result_flag]
                result_flag += 1
                flag_j -= 1
            parameter = temp2 / operate_line[flag_rol]
            parameters.append(parameter)
        flag_rol -= 1
        i -= 1
    return parameters


paremeters = [[6, 15, 55, 152.6],
              [15, 55, 225, 585.6], 
              [55, 225, 979, 2488.8]]
results = calculate_parameter(paremeters)
print(" x1=" + str(results[2]) + "\n x2=" + str(results[1]) + "\n x3=" + str(results[0]))