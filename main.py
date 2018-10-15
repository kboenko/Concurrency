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
    res[i] = sum(arr)
    time.sleep(1)
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

    while first + step <= numbersQty:
        t = Thread(target=sum_arr, name = 'Thread #' + str(i), args=(i, floatNums[first : last], results))
        t.start()
        first += step
        last += step
        i += 1

        if first + step > numbersQty and part > 0:
            t = Thread(target=sum_arr, name='Thread #' + str(i), args=(i, floatNums[first:], results))
            t.start()

    for i in results.keys():
        summa += results[i]

    print(summa)
    print(sum(floatNums))

    return summa

sum_numbers(31, 5)

print(simpleSum())