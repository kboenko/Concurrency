from threading import Thread
from random import random
from random import randint
import time

nums = []

def simpleSum():
    return sum(nums)

def generate(qty):
    #return [random() * 10 for number in range(1, qty + 1)]
    return [randint(1,10) for number in range(1, qty + 1)]

def sum_arr(i, arr, res):
    s_arr = 0
    for j in arr:
        s_arr += j
        print(str(i) + ': ' + str(s_arr))
        time.sleep(1)

    res[i] = s_arr
    print('Cумма массива ' + str(i) + ': ' + str(res[i]))

    return res

def sum_numbers(numbersQty, threadQty):
    floatNums = generate(numbersQty)

    #global list for testing
    global nums
    nums = floatNums

    whole = int(numbersQty / threadQty)
    part = numbersQty % threadQty

    step = 0

    if part == 0:
        step = whole
    else:
        step = int(numbersQty / (threadQty - 1))

    first = 0
    last = step
    i = 1
    summa = 0
    results = {}
    threads = []

    while first + step <= numbersQty:
        t = Thread(target=sum_arr, name = 'Thread #' + str(i), args=(i, floatNums[first : last], results))
        t.start()
        threads.append(t)
        first += step
        last += step
        i += 1

        if first + step > numbersQty and part > 0:
            t = Thread(target=sum_arr, name='Thread #' + str(i), args=(i, floatNums[first:], results))
            t.start()
            threads.append(t)

    while True:
        for thr in threads:
            if not thr.isAlive():
                threads.remove(thr)
        time.sleep(1)
        if len(threads) == 0:
            print('Больше нет работающих тредов!')
            break

    for i in results.keys():
        summa += results[i]

    print('*******************')
    print(summa)
    print('*******************')
    print(sum(floatNums))

    return summa

sum_numbers(31, 5)

print(simpleSum())