# -*- encoding:utf-8 -*-
"""
    author:lgh
"""

import os
import numpy as np
from PIL import Image


class SmallPic(object):
    """
        a small picture spliced to a large picture
    """

    def __init__(self, dir):
        self.dir = dir
        self.size = (20, 20)
        self.img = Image.open(dir).resize(self.size)
        self.avg_color = (0,0,0)
        self.data = list()

    def get_img(self):
        """
            get picture
        :return: PIL object, a picture opened with PIL
        """
        return self.img

    def get_size(self):
        """
            get size
        :return: tuple, (w, h)
        """
        return self.size

    def set_avg_color(self, color):
        """
            set picture average color
        :param color: average color
        :return: None
        """
        self.avg_color = color

    def get_avg_color(self):
        """
            get average color
        :return: tuple, (r,g,b)
        """
        return self.avg_color

    def get_data(self):
        """
            get picture data and set average color
        :return: list, picture data
        """
        datas = self.img.getdata()
        w, h = self.get_size()
        r_avg_color = 0
        g_avg_color = 0
        b_avg_color = 0
        self.data = list()
        for i in range(len(datas)):
            r_avg_color += datas[i][0]
            g_avg_color += datas[i][1]
            b_avg_color += datas[i][2]
            self.data.append(datas[i])
        r_avg_color = r_avg_color // len(datas)
        g_avg_color = g_avg_color // len(datas)
        b_avg_color = b_avg_color // len(datas)
        self.set_avg_color((r_avg_color, g_avg_color, b_avg_color))
        return self.data

    def get_changed_data(self, loss_color):
        """
            picture add loss color
        :param loss_color: tuple, (r,g,b)
        :return: array
        """
        datas = np.array(self.get_data())
        changed_data = datas + loss_color
        changed_data = changed_data.tolist()
        for i in range(len(changed_data)):
            changed_data[i] = tuple(changed_data[i])
        return changed_data


def get_box(w, h, i, t_w):
    if i == 0:
        x1, x2, x3, x4 = (0, 0, w, h)
    else:
        remain = i % t_w
        if remain != 0:
            num = i // t_w
            x1 = remain * w
            x2 = num * h
        else:
            num = i // t_w
            x1 = 0
            x2 = num * h
    x3 = x1 + w
    x4 = x2 + h
    return (x1, x2, x3, x4)

def main():
    base_dir = r'F:\\classfication'
    target_dir = r'F:\\touxiang.jpg'
    target_size = (100, 80)
    files = os.listdir(base_dir)
    dir = os.path.join(base_dir, files[0])
    img = SmallPic(dir)
    target = Image.open(target_dir)
    target = target.resize(target_size)
    avg_color = img.get_avg_color()
    w, h = img.get_size()
    t_w, t_h = target_size
    new_img = Image.new('RGB', (w * t_w, h * t_h))
    for i in range(len(target.getdata())):
        loss_color = abs(np.array(target.getdata()[i]) - np.array(avg_color))
        changed_data =img.get_changed_data(loss_color)
        tmp_img = Image.new('RGB', img.get_size())
        tmp_img.putdata(changed_data)
        box = get_box(w, h , i, t_w)
        new_img.paste(tmp_img, box)
    new_img.show()

if __name__ == '__main__':
    main()