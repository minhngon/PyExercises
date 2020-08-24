#!/usr/bin/env python3

'''
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]
'''


def solve():
    '''Trả về list chứa các list là các bộ số thỏa mãn đề bài

    Ví dụ:
        [[9, 1, 1], ..., [1, 9, 1]]

    Lưu ý: kết quả từng list con trả về với a giảm dần, b và c tăng dần
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    #raise NotImplementedError("Học viên chưa làm bài này")
    result = action()
    return result

def action():
    max, result = 10, 10
    min = 1
    arr = []
    for a in range(max-1,min-1,-1):
        cal = result - a
        for b in range(cal, max, cal):
            c = (b / (result-a))
            if c%1==0 and a + (b / c) == result:
                arr.append([a, b, int(c)])
    return arr
def main():
    print(solve())


if __name__ == "__main__":
    main()
