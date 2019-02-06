'''
Read an integer .
Without using any string methods, try to print the following:

Note that "" represents the values in between.
'''
from aetypes import end

if __name__ == '__main__':
    n = int(input())
    def name(input_number):
        for i in range(1,input_number+1):
            print(i, end(''))
    name(n)