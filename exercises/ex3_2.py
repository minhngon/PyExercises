#!/usr/bin/env python3
import time

data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''
# https://www.poetrysoup.com/poem/cross_my_heart_609765


def solve(input_data):
    '''Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
    Chỉ viết hoa chữ cái đầu tiên.
    '''
    result = None

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")
    temp = input_data.split('\n')
    start1 = time.time()
    string = ''
    string2 = ''
    for i in range(1000):
        for item in temp:
            if item[:1].isupper():
                string += item[:1]
        string2 += string
    result = string
    end1 = time.time()
    print(end1-start1)
    
    start2 = time.time()
    string3 = []
    for i in range(1000):
        av = ''.join(i[:1] for i in temp if i[:1].isupper())
        string3.append(av)
    result = ''.join(string3)
    end2 = time.time()

    print(end2-start2)
    
    

    return None


def main():
    '''
    Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    '''
    print(solve(data))


if __name__ == "__main__":
    main()
