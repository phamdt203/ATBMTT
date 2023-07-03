import sys, os

def read_file(path):
    fo = open(path)
    contents = fo.read().split(',')
    fo.close()
    return (contents[0], contents[1], contents[2], contents[3])

def save_file(path, keySize, n, e, d):
    fo = open(path, 'w')
    fo.write(','.join([keySize, n, e, d]))
    fo.close()
    return()

def read_input(path):
    fo = open(path, 'r', encoding= 'utf8')
    contents = fo.read()
    fo.close()
    return contents

def save_input(path, content):
    fo = open(path, 'w', encoding='utf8')
    fo.write(content)
    fo.close()
    return()