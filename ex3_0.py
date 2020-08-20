#!/usr/bin/env python3
data = 5


def squared(input_data):
    """Tính bình phương của số đầu vào

    Số đầu vào ở đây được chứa trong tên `input_data`,
    được cung cấp sẵn bởi bài tập. Học viên chỉ cần lo tính toán ra kết quả
    dựa trên `input_data` đã cho.
    """
    
    return pow(input_data, 2)


def main():
    print(squared(data))


if __name__ == "__main__":
    main()
