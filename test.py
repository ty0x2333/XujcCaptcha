from __future__ import division

import os

import Image

from XujcCaptcha import XujcCaptcha

# Colors
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'


def print_with_color(str, color):
    print string_with_color(str, color)


def string_with_color(str, color):
    return '%s%s%s' % (color, str, ENDC)


def print_error(answer, result):
    print '%s answer: %s, but result is %s.' % (string_with_color('[Error]', RED),
                                                string_with_color(answer, BLUE),
                                                string_with_color(result, RED))


def print_statistics(total, success_count):
    correct_rate = success_count * 100 / total
    error_count = total - success_count
    print 'correct rate: %s, total: %s, success: %s, error: %s' % (string_with_color('%.2f%%' % correct_rate, BLUE),
                                                                   string_with_color(str(total), BLUE),
                                                                   string_with_color(str(success_count), GREEN),
                                                                   string_with_color(str(error_count), RED))

if __name__ == '__main__':
    captcha = XujcCaptcha()

    total = 0
    success_count = 0
    for filename in os.listdir('./test_images'):
        file_path = os.path.join('./test_images', filename)
        # print os.path.basename(fp)
        (name, suffix) = os.path.splitext(filename)
        image = Image.open(file_path)
        result = captcha.recognition(image)
        if result == name:
            print_with_color('[Pass] %s' % result, GREEN)
            success_count += 1
        else:
            print_error(name, result)

        total += 1

    print_statistics(total, success_count)