# -*- encoding:utf-8 -*-
"""
    change pic into char pic
    author:lgh
"""

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
WIDTH = 160
HIGHT = 120

def get_char(r,g,b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]

def test():
    im = Image.open(r'test.png')
    im = im.resize((WIDTH, HIGHT), Image.NEAREST)
    w, h = im.size
    txt = ''
    for i in range(len(im.getdata())):
        txt += get_char(*im.getdata()[i])
        if i % w == 0:
            txt += '\n'
    print(txt)

    # with open('output.txt', 'w') as f:
    #     f.write(txt)

if __name__ == '__main__':
    test()