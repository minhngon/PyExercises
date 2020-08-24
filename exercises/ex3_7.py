#!/usr/bin/env python3

'''
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
'''


def solve():
    '''Trả về 1 `list` các `string` có dạng:

        output: ['5 == 1 * 5', '10 == 2 * 5', ...]

    Lưu ý: Thứ tự tăng dần theo bảng cửu chương
    '''
    result = None
    arr = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    for i in range(0,100):
        res = calculate(i,5)
        if res != None:
            arr.append(res)
    result = arr
    return result

def calculate(n,i):
    if n % i == 0:
        return str(n) + " == " + str(n // i) + " * " + str(i)
    
def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
