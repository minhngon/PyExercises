#!/usr/bin/env python3
import datetime
'''
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    '''Trả về 1 `list` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: list
    '''
    assert (input_data in range(1, 13, 1)), "Tháng không tồn tại"
    result = ["MONTH", "DATE"]

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    result = Num2String(input_data)
    return result


def Num2String(n):
    year = 2020
    day = 1
    if n > 0 and n < 12:
        date1 = datetime.datetime(year, n, day)
        date2 = datetime.datetime(year, n+1, day)
        return [date1.strftime("%B"), (date2-date1).days]
    elif n == 12:
        date1 = datetime.datetime(year, n, day)
        date2 = datetime.datetime(year+1, 1, day)
        return [date1.strftime("%B"), (date2-date1).days]
    else:
        return "Tháng không tồn tại"


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
