Xujc Captcha
===
Get Start
---
1. install PIL

  Debian:
  ```shell
$ sudo apt-get install python-imaging
  ```
  OS X or Other Linux:
  ```shell
$ sudo easy_install PIL
  ```
  Other platform:

  see [PIL Home](http://www.pythonware.com/products/pil/index.htm)

2. install pytesser

  ```shell
$ sudo apt-get install tesseract-ocr
$ sudo pip install pytesseract
  ```
3. copy traindata

  copy traindata/xujc.traineddata to your/tesseract-ocr/path/tessdata/xujc.traineddata

  eg. Ubuntu:

  usr/share/tesseract-ocr/tessdata/xujc.traineddata
