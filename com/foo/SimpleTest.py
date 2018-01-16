# -*- coding: utf-8 -*-

# 测试是否是素数
def getSu(start, end):
    for i in range(start, end + 1):
        for j in range(2,i):
            if i % j == 0:
                k = i / j;
                print (i, "==", j, "*", k)
                break;
            else:
                continue
        if i == j +1:
            print(i, "is prime number !")

getSu(100, 200)


# 测试占位符
def testStr():
    print "hello, my name is {}, age is {}".format("wangzheng", 10)

testStr();

