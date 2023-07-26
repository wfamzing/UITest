import json
import os

import ddddocr
import requests

def ocrCaptcha():
    ocr = ddddocr.DdddOcr()
    cPath = os.getcwd()
    print(cPath)
    img_file = './code.png'
    with open(img_file, 'rb') as f:
        print("file", f)
        img_bytes = f.read()

    # 通过ddddocr进行识别验证码
    res = ocr.classification(img_bytes)
    print("验证码："+res)
    return res

