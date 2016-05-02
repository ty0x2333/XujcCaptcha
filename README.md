Xujc Captcha
===
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
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
3. copy training_data

  copy `training_data/xujc.traineddata` to `your/tesseract-ocr/path/tessdata/xujc.traineddata`

  eg. Ubuntu:

  ```shell
  $ sudo cp ./training_data/xujc.traineddata /usr/share/tesseract-ocr/tessdata/xujc.traineddata
  ```
4. run test script

  ```shell
  $ python test.py
  ```

F&Q
---
1. pytesseract.pytesseract.TesseractError: (1, 'Error opening data file /usr/share/tesseract-ocr/tessdata/xujc.traineddata')

  Make sure that you have copied the `tessdata/xujc.traineddata` file to `/usr/share/tesseract-ocr/tessdata`

License
---
XujcCaptcha is available under the MIT license. See the LICENSE file for more info.
