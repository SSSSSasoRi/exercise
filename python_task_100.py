def python_task_002(i):
    result = 0
    while i > 0:
        if i > 1000000:
            result += (i - 1000000) * 0.01
            i = 1000000
        elif i > 600000:
            result += (i - 600000) * 0.015
            i = 600000
        elif i > 400000:
            result += (i - 400000) * 0.03
            i = 400000
        elif i > 200000:
            result += (i - 200000) * 0.05
            i = 200000
        elif i > 100000:
            result += (i - 100000) * 0.075
            i = 100000
        else:
            result += i * 0.1
            i = 0
    return result


year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for idx in range(1, len(months)):
    months[idx] += months[idx - 1]

res = 0
if 0 < month <= 12:
    res = months[month - 1]
else:
    print("data error")
res += day

leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if month > 2:
    res += leap

print(f"it is the {res}th day.")
