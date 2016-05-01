# -*- coding: utf-8 -*-
import Image, ImageDraw
from pytesseract import *


def check(xy, img, matrix):
    try:
        return img.getpixel(xy) < 255 and matrix[xy[0]][xy[1]] != -1
    except:
        return False


def juli(r,s):
    return abs(r[0]-s[0])+abs(r[1]-s[1])+abs(r[2]-s[2])


def clear_noise(img):
    width = img.size[0]
    height = img.size[1]
    matrix = [-1] * width
    for i in range(len(matrix)):
        matrix[i] = [-1] * height

    maps = {}
    n = 0

    for y in xrange(0, height):
        for x in xrange(0, width):
            center = (x, y)
            left = (x - 1, y)
            right = (x + 1, y)
            top = (x, y - 1)
            bottom = (x, y + 1)
            left_bottom = (x - 1, y + 1)
            right_bottom = (x + 1, y + 1)
            left_top = (x - 1, y - 1)
            right_top = (x + 1, y - 1)
            r = [0, 0, 0]
            s = [0, 0, 0]
            if img.getpixel(center) < 255:
                if check(left, img, matrix):# left
                    matrix[x][y] = matrix[x - 1][y]
                    maps[str(matrix[x][y])] += 1
                elif check(left_top, img, matrix):# left-top
                    matrix[x][y] = matrix[x - 1][y - 1]
                    maps[str(matrix[x][y])] += 1
                elif check(top, img, matrix):# top
                    matrix[x][y] = matrix[x][y - 1]
                    maps[str(matrix[x][y])] += 1
                elif check(right_bottom, img, matrix):# right-bottom
                    matrix[x][y] = matrix[x + 1][y + 1]
                    maps[str(matrix[x][y])] += 1
                elif check(bottom, img, matrix):# bottom
                    matrix[x][y] = matrix[x][y + 1]
                    maps[str(matrix[x][y])] += 1
                elif check(left_bottom, img, matrix):# left-bottom
                    matrix[x][y] = matrix[x-1][y + 1]
                    maps[str(matrix[x][y])] += 1
                elif check(right_top, img, matrix):# right-top
                    matrix[x][y] = matrix[x+1][y - 1]
                    maps[str(matrix[x][y])] += 1
                elif check(right, img, matrix):# right
                    matrix[x][y] = matrix[x + 1][y]
                    maps[str(matrix[x][y])] += 1
                else:
                    n+=1
                    maps[str(n)]=1
                    matrix[x][y] = n

    for x in range(width):
        for y in range(height):
            if matrix[x][y] != -1 and maps[str(matrix[x][y])] <= 2:
                img.putpixel((x, y), 255)


if __name__ == '__main__':
    image = Image.open(r'./test_images/WWBS.png')
    # convert to Gray Scale Image
    gray_img = image.convert('L')
    gray_img.save(r'./gray.png')

    print 'image size:', gray_img.size

    print image_to_string(gray_img, lang='xujc')

    clear_noise(gray_img)

    # convert to Binary Image
    threshold = 200
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    gray_img = gray_img.point(table, '1')
    gray_img.save(r'./clear_noise.png')

    print image_to_string(gray_img, lang='xujc')



