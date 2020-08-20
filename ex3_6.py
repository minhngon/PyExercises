#!/usr/bin/env python3

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""


def solve(input_data):
    """Trả về 1 `list` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
    assert input_data in range(1, 13, 1), "Tháng không tồn tại"
    result = {
            1: ['January', 31],
            2: ['February', 28],
            3: ['March', 31],
            4: ['April', 30],
            5: ['May', 31],
            6: ['June', 30],
            7: ['Julynuary', 31],
            8: ['August', 31],
            9: ['September', 30],
            10: ['October', 31],
            11: ['November', 30],
            12: ['December', 31],
            }

    return result[input_data]


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
