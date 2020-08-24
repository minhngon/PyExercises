#!/usr/bin/env python3

'''
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.
'''


def solve():
    '''Thay vì in ra, hãy trả về 1 `list`
    100 phần tử thỏa mãn yêu cầu đề bài

    :rtype: list
    '''
    result = None
    arr = []
    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    for i in range(1, 100):
        if (BoiCua3(i) and BoiCua5(i)):
            arr.append(str(i) + ": FizzBuzz")
        elif (BoiCua3(i)):
            arr.append(str(i) + ": Fizz")
        elif (BoiCua5(i)):
            arr.append(str(i) + ": Buzz")
        else:
            arr.append(str(i))
    result = arr
    return result


def BoiCua3(n):
    if (n % 3 == 0):
        return True
    return False


def BoiCua5(n):
    if (n % 5 == 0):
        return True
    return False


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
