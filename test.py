

import requests


req = requests.get('https://github.com')
print(req.status_code)
