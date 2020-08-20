#!/usr/bin/env python3

"""
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.
"""


def solve():
    """Thay vì in ra, hãy trả về 1 `list`
    100 phần tử thỏa mãn yêu cầu đề bài

    :rtype: list
    """

    return ['FizzBuzz' if index % 3 == 0 and index % 5 == 0
            else 'Fizz' if index % 3 == 0
            else 'Buzz' if index % 5 == 0
            else index
            for index in range(1, 101)]


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()