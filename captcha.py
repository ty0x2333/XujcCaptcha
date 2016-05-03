from optparse import OptionParser
import logging
import Image
from XujcCaptcha import *
__version__ = "1.0"


def main():
    parser = OptionParser(usage='%prog filename [options] arg',
                          version='%prog ' + __version__,
                          description='recognition captcha for http://jw.xujc.com/')
    parser.add_option('-v', '--verbose', action="store_true", dest="verbose", help="verbose")
    parser.add_option('-t', '--threshold', default=DEFAULT_THRESHOLD, dest="threshold", help="threshold for binary image (default:%default)")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error('filename not given')

    if options.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level, format='%(message)s',)

    parser.get_default_values()

    filename = args[0]
    logging.info('recognition file: %s' % filename)

    image = Image.open(filename)
    logging.info('image size: %s' % str(image.size))
    logging.info('threshold: %d' % options.threshold)

    captcha = XujcCaptcha(options.threshold)
    print captcha.recognition(image)


if __name__ == '__main__':
    main()
