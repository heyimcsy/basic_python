def bus_rate(age):
    if age > 65:
        print('무료입니다.')
    elif age > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')

bus_rate(24)


def check_gender(pin):
    checkPin = pin.split('-')[1][:1]
    if(int(checkPin) == 2):
        print('여성',pin)
    else:
        print('남성', pin)

check_gender('120101-1023133')
check_gender('120101-2023133')
check_gender('121121-2323133')