# -*- coding: utf-8 -*-


def testReadFile():
    """

    :rtype: object
    """
    f = open("E://readme.txt", 'r')
    lines = f.readlines()
    for line in lines:
        print line.decode("utf-8").encode("utf-8")

testReadFile()