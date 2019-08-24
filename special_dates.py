import math

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = [31, 30, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31]


def primality_test(n):
    for i in range(2, int(math.sqrt(n))):
        if not n%i:
            return False
    return True


count = 0
for year in range(0, 2020):
    for month in range(12):
        for day in range(1, days[month]+1):
            date = str(year) + str(months[month]) + (('0'+str(day)) if len(str(day)) == 1 else str(day))
            number = date[:]
            success = True
            while len(number) and success:
                if not primality_test(int(number)):
                    success = False
                number = number[1:]
            if success:
                #print(date)
                count += 1
print('Total:', count)

