# coding: utf-8

# Пример работы с JSON

import json

def _gen_data():
    import time
    import hashlib
    import random

    t = time.time()

    return {
        'timestamp':  int(t),
        'payload': hashlib.md5(str(t + random.random())).hexdigest(),
    }

def main():
    data = []
    for i in range(100):
        data.append(_gen_data())

    print json.dumps(data, indent=1)

    x = '''
{"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}  
    '''

    d = json.loads(x)

    print d['widget']['image']['src']

if __name__ == "__main__":
    main()
