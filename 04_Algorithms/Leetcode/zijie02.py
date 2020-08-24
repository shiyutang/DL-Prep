cases = int(input())
for i in range(cases):
    string = input()
    p = 0
    initlen = len(string)
    while p + 3 < len(string):
        tmp = string[p:p + 4]
        if tmp == '0010':
            if p + 6 < len(string) and string[p + 4:p + 7] in ('000', '001', '010', '011', '100', '101', '110', '111'):
                if string[p + 4:p + 7] == '010':
                    string = string[:p + 3] + string[p + 4:]
                    string = string[:p + 3] + string[p + 4:]
                elif string[p + 4] == '0':
                    string = string[:p + 2] + string[p + 3:]
                else:
                    string = string[:p + 3] + string[p + 4:]

            elif p + 5 < len(string) and string[p + 4:p + 6] in ('00', '01', '10', '11'):
                if string[p + 4:p + 6] == '10':
                    string = string[:p + 3] + string[p + 4:]
                else:
                    string = string[:p + 2] + string[p + 3:]
            elif p + 4 < len(string) and string[p + 4] in ('0', '1'):
                if string[p + 4] == '0':
                    string = string[:p + 2] + string[p + 3:]
                else:
                    string = string[:p + 3] + string[p + 4:]
            else:
                string = string[:p + 3] + string[p + 4:]

        else:
            p += 1
    # print(string)
    print(initlen - len(string))


# 8
# 01001010
# 00101
# 00100
# 00100010
# 00100010010
# 0010
# 0010001
# 0010010

# zijie0823