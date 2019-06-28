import math
import os
import sys

import requests

print(sys.executable)
test = 'hello'


def greet(who_to_greet):
    print('hello ' + who_to_greet)


req = requests.get('https://github.com')
print(req.status_code)
