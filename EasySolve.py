def avg(lists):
    hap = 0
    for a in lists:
        hap += a
    result = hap / len(lists)
    return result


def mid(lists):
    if len(lists) % 2 == 0:
        middle_first = int(len(lists) / 2)
        middle_second = middle_first + 1
        result = (lists[middle_first - 1] + lists[middle_second - 1]) / 2
        return result
    else:
        middle = int(len(lists) / 2)
        result = lists[middle]
        return result


def frq(lists):
    frequency = list()
    for i in lists:
        cnt = 0
        for j in lists:
            if i == j:
                cnt += 1
        frequency.append(cnt)
    result = lists[frequency.index(max(frequency))]
    return result


inputs = list()
numbers = list()
number = 0

print(" >> EasySolve")
print(" 숫자를 하나씩 입력하시고 다 입력하시면 엔터키를 한 번 더 누르세요.")
print("=====================================================================")

# 정렬
while number is not "":
    number = input(" 숫자 입력 : ")
    inputs.append(number)
inputs.pop()
for i in inputs:
    numbers.append(int(i))

numbers.sort()

# 출력
count = 0
for i in numbers:
    if count % 10 == 0:
        print()
        print(" ", end="")
    print("%2d" % i, end=" ")
    count += 1

print("\n 총 %d개의 숫자 중에서..." % len(numbers))
print("=====================================================================")
print(" 최솟값 :", min(numbers))
print(" 최댓값 :", max(numbers))
print("---------------------------------------------------------------------")
print(" 평균   :", avg(numbers))
print(" 중간값 :", mid(numbers))
print(" 최빈값 :", frq(numbers))
frq(numbers)
input()
