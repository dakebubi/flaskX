# -*- coding: utf-8 -*-
def testReadFile():
    """
    :rtype: object
    """
    f = open("/readme.txt", 'r')
    lines = f.readlines()
    for line in lines:
        print line.decode("utf-8").encode("utf-8")


# 测试是否是素数
def getSu(start, end):
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                k = i / j;
                print (i, "==", j, "*", k)
                break;
            else:
                continue
        if i == j + 1:
            print(i, "is prime number !")


# 测试占位符
def testStr():
    print "hello, my name is {}, age is {}".format("fangfang", 10)
